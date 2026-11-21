#!/usr/bin/env python3
"""Ask the staff advisors their test questions and grade the answers.

    run.py                    every case
    run.py cfo accountant     only these roles or case ids
    run.py --baseline cfo     the same questions to plain Claude with no advisor,
                              to check the advisor is worth its cost
    run.py --baseline --pointer cfo
                              the fair control: plain Claude told to read the brief first.
                              An advisor earns its cost only where it beats this one.

Each case in cases.json (or --cases FILE) is a question with a checklist: what a good answer must
do and must not do. The advisor answers from the case's working directory, so
it reads that project's .claude/company.md. A cheap judge model then checks
each item. Answers and grades are saved in runs/<timestamp>/.

    run.py --compare OLD NEW  pair two runs (folder names in runs/) case by case: regressed,
                              improved, held pass, held fail, not graded. A case whose question
                              or checklist was edited is never compared. Exit 1 when a case regressed.

Each run writes results.json: per case its status, its trials, and 12-character SHA-256
fingerprints of the case and of the advisor file. Runs made before this have none.

    run.py --trials 3 legal   ask each case 3 times; it passes only if all 3 do,
                              because one good answer can be luck

Exit code 0 when every case passes, 1 when one fails, 2 when one could not be
graded (usage limit, crash): an ERROR is not a failure, rerun it.
"""
import argparse
import concurrent.futures as cf
import os
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
# The advisors' shared files: staff/ beside this folder (repo or plugin), or the parent folder when installed as ~/.claude/staff/evals.
STAFF = pathlib.Path(os.environ.get("STAFF_DIR", HERE.parent / "staff" if (HERE.parent / "staff").is_dir() else HERE.parent)).expanduser()
# A plugin install names its agents <plugin>:<agent>; set ADVISOR_PREFIX=founder-advisors: for that.
PREFIX = os.environ.get("ADVISOR_PREFIX", "")
# The advisor files: staff/agents beside this folder (repo or plugin), else ~/.claude/agents/staff (installed).
AGENTS = STAFF / "agents" if (STAFF / "agents").is_dir() else pathlib.Path.home() / ".claude/agents/staff"
# Known gap: Bash(python3 *) still lets an advisor write files through python3 -c, past the Write/Edit block below.
TOOLS = "Read,Grep,Glob,WebSearch,WebFetch,Bash(python3 *)"
# --pointer: the fair control. Plain Claude gets the one line a project's CLAUDE.md would need.
POINTER = "Before answering, read the company brief at .claude/company.md and the files it lists for this question."


def project_memory(cwd: pathlib.Path) -> pathlib.Path:
    # Claude Code keeps a project's auto-memory under a path-derived folder name.
    return pathlib.Path.home() / ".claude/projects" / re.sub(r"[^A-Za-z0-9]", "-", str(cwd)) / "memory"


def build_cmd(case, baseline, pointer=False, model=None):
    cwd = pathlib.Path(case["cwd"]).expanduser()
    cmd = ["claude", "-p", "--no-session-persistence", "--permission-mode", "dontAsk",
           "--allowedTools", TOOLS, "--add-dir", str(STAFF), "--add-dir", str(project_memory(cwd)),
           # Advisors with `memory: user` get Write/Edit automatically. A test run must not
           # leave memories behind: the advisor would later recall test questions as the founder's.
           "--disallowedTools", "Write,Edit,NotebookEdit",
           # Plain -p prints only the last assistant message. An advisor that answers, then tries
           # to write memory and is refused, ends with "memory unavailable" and the answer is lost.
           # Stream every message and join all the assistant text instead.
           "--output-format", "stream-json", "--verbose"]
    if model:
        cmd += ["--model", model]  # the advisor and its baseline use the same model; overrides the agent file's model: line
    if not baseline:
        cmd += ["--agent", PREFIX + case["role"]]
    elif pointer:
        cmd += ["--append-system-prompt", POINTER]
    return cmd


def ask(case, baseline, pointer=False, model=None):
    cwd = pathlib.Path(case["cwd"]).expanduser()
    cmd = build_cmd(case, baseline, pointer, model)
    # The question goes on stdin: --add-dir takes several values and would swallow it.
    out = subprocess.run(cmd, input=case["question"], cwd=cwd, capture_output=True, text=True, timeout=1500)
    texts = []
    for line in out.stdout.splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "assistant":
            for block in ev.get("message", {}).get("content", []):
                if block.get("type") == "text" and block.get("text", "").strip():
                    texts.append(block["text"].strip())
    return "\n\n".join(texts) or f"(no answer; stderr: {out.stderr.strip()[:500]})"


def judge(case, answer, model):
    must = "\n".join(f"{i}. {c}" for i, c in enumerate(case["must"], 1))
    must_not = "\n".join(f"{i}. {c}" for i, c in enumerate(case.get("must_not", []), 1))
    prompt = f"""Grade an answer against a checklist. Be strict and literal; judge substance, not style or length.

QUESTION:
{case["question"]}

ANSWER:
<<<
{answer}
>>>

MUST items (met = the answer does this):
{must}

MUST-NOT items (met = the answer DOES this forbidden thing):
{must_not or "(none)"}

Reply with JSON only, no prose. "must" holds exactly {len(case["must"])} entries (n = 1..{len(case["must"])}) and "must_not" exactly {len(case.get("must_not", []))}; never put a MUST-NOT grade under "must":
{{"must":[{{"n":1,"met":true,"why":"short quote or reason"}}],"must_not":[{{"n":1,"met":false,"why":"..."}}]}}"""
    out = subprocess.run(["claude", "-p", "--no-session-persistence", "--model", model, "--tools", ""],
                         input=prompt, capture_output=True, text=True, timeout=300)
    match = re.search(r"\{.*\}", out.stdout, re.S)
    if not match:
        return {"error": out.stdout.strip()[:500] or out.stderr.strip()[:500]}
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError as e:
        return {"error": f"judge reply not JSON ({e}): {match.group(0)[:300]}"}


def misfiled(case, grade):
    # The judge must grade each item exactly once, under its own list. Haiku sometimes files
    # the must_not grades under "must" (10 Oct 2026), which read as a FAIL or crashed the run.
    def bad(graded, items):
        return len(graded) != len(items) or {g.get("n") for g in graded} != set(range(1, len(items) + 1))
    return bad(grade.get("must", []), case["must"]) or bad(grade.get("must_not", []), case.get("must_not", []))


def passed(case, grade):
    if "error" in grade:
        return "ERROR", ["judge failed: " + grade["error"]]
    if misfiled(case, grade):
        return "ERROR", ["judge misfiled the checklist"]
    misses = [f"missing: {case['must'][g['n'] - 1]}" for g in grade["must"] if not g.get("met")]
    misses += [f"did: {case['must_not'][g['n'] - 1]}" for g in grade.get("must_not", []) if g.get("met")]
    return ("FAIL" if misses else "PASS"), misses


# An answer that never happened (usage limit, crash) is an infrastructure error, not a failed case.
NO_ANSWER = re.compile(r"^\(no answer|hit your \w+ limit", re.I | re.M)


def digest(data):
    raw = data if isinstance(data, bytes) else json.dumps(data, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()[:12]


def fingerprint(case, baseline):
    agent = AGENTS / f"{case['role']}.md"
    return {"case": digest(case), "baseline": baseline,
            "advisor": None if baseline or not agent.exists() else digest(agent.read_bytes())}


def overall(statuses):
    return "ERROR" if "ERROR" in statuses else "PASS" if all(s == "PASS" for s in statuses) else "FAIL"


def compare(old, new):
    """Pair two runs' results.json by case id: [(case id, verdict, advisor file changed)]."""
    rows = []
    for cid in sorted(old.keys() & new.keys()):
        a, b = old[cid], new[cid]
        if a["case"] != b["case"]:
            verdict = "edited"  # the question or checklist changed: the two grades measure different things
        elif "ERROR" in (a["status"], b["status"]):
            verdict = "not graded"
        elif a["status"] == b["status"]:
            verdict = "held " + a["status"].lower()
        else:
            verdict = "regressed" if a["status"] == "PASS" else "improved"
        changed = not a["baseline"] and not b["baseline"] and a["advisor"] != b["advisor"]
        rows.append((cid, verdict, changed))
    return rows


def load_results(name):
    d = pathlib.Path(name) if pathlib.Path(name).is_dir() else HERE / "runs" / name
    f = d / "results.json"
    if not f.exists():
        sys.exit(f"{d}: no results.json (older runs have none)")
    return json.loads(f.read_text())


def report(old_name, new_name):
    old, new = load_results(old_name), load_results(new_name)
    if {r["baseline"] for r in old.values()} != {r["baseline"] for r in new.values()}:
        print("Note: one run is a baseline (plain Claude), the other the advisor.")
    rows = compare(old, new)
    for cid, verdict, changed in rows:
        print(f"{verdict:11} {cid}" + ("  (advisor file changed)" if changed else ""))
    for label, ids in (("only in " + old_name, old.keys() - new.keys()), ("only in " + new_name, new.keys() - old.keys())):
        if ids:
            print(f"{label}: {', '.join(sorted(ids))}")
    regressed = sum(v == "regressed" for _, v, _ in rows)
    print(f"\n{len(rows)} paired, {regressed} regressed, {sum(v == 'improved' for _, v, _ in rows)} improved, "
          f"{sum(v == 'edited' for _, v, _ in rows)} edited (not compared)")
    sys.exit(1 if regressed else 0)


def run(case, baseline, model, outdir, trial, pointer=False, advisor_model=None):
    answer = ask(case, baseline, pointer, advisor_model)
    if NO_ANSWER.search(answer[:300]):
        grade = {"error": answer[:300]}
    else:
        grade = judge(case, answer, model)
        if "error" not in grade and misfiled(case, grade):
            grade = judge(case, answer, model)  # one more judge call is far cheaper than a new advisor run
    status, misses = passed(case, grade)
    name = case["id"] + (f".t{trial}" if trial > 1 else "")
    (outdir / f"{name}.md").write_text(
        f"# {case['id']} ({'baseline' if baseline else case['role']}, model: {advisor_model or 'default'})\n\n**Q:** {case['question']}\n\n"
        f"{answer}\n\n---\n```json\n{json.dumps(grade, ensure_ascii=False, indent=1)}\n```\n")
    return case, status, misses


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("only", nargs="*", help="roles or case ids to run")
    ap.add_argument("--baseline", action="store_true", help="ask plain Claude instead of the advisor")
    ap.add_argument("--pointer", action="store_true",
                    help="with --baseline: tell plain Claude to read .claude/company.md first (the fair control)")
    ap.add_argument("--model", help="model for the advisor or the baseline, to test a cheaper model against the same cases")
    ap.add_argument("--judge", default="haiku", help="judge model (default haiku)")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--cases", default=HERE / "cases.json", type=pathlib.Path,
                    help="cases file (default cases.json; start from cases.example.json)")
    ap.add_argument("--trials", type=int, default=1,
                    help="ask each case N times; a case passes only if every trial passes (pass^k)")
    ap.add_argument("--compare", nargs=2, metavar=("OLD", "NEW"), help="pair two runs (folder names in runs/) by case")
    args = ap.parse_args()
    if args.compare:
        report(*args.compare)
    if args.pointer and not args.baseline:
        ap.error("--pointer needs --baseline")

    if not args.cases.exists():
        sys.exit(f"{args.cases} not found: copy cases.example.json to cases.json and write your own cases")
    cases = json.loads(args.cases.read_text())
    if args.only:
        cases = [c for c in cases if c["role"] in args.only or c["id"] in args.only]
    if not cases:
        sys.exit("no matching cases")
    for c in cases:
        # A MUST item phrased as a prohibition confuses the judge (met = the answer does it).
        for m in c["must"]:
            if re.match(r"(?i)(does not|doesn't|never|no )", m):
                sys.exit(f"{c['id']}: MUST item is a prohibition; move it to must_not: {m}")

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ("-baseline" if args.baseline else "") + ("-pointer" if args.baseline and args.pointer else "")
    outdir = HERE / "runs" / stamp
    outdir.mkdir(parents=True)

    results = {}  # case id -> statuses of its trials
    jobs = [(c, t) for c in cases for t in range(1, args.trials + 1)]
    with cf.ThreadPoolExecutor(args.jobs) as pool:
        for case, status, misses in pool.map(lambda j: run(j[0], args.baseline, args.judge, outdir, j[1], args.pointer, args.model), jobs):
            results.setdefault(case["id"], []).append(status)
            print(f"{status:5} {case['id']}")
            for m in misses:
                print(f"      {m}")
    by_id = {c["id"]: c for c in cases}
    (outdir / "results.json").write_text(json.dumps(
        {cid: {"status": overall(r), "trials": r, **fingerprint(by_id[cid], args.baseline)} for cid, r in results.items()},
        indent=1, ensure_ascii=False))
    passes = sum(all(s == "PASS" for s in r) for r in results.values())
    errors = sum("ERROR" in r for r in results.values())
    if args.trials > 1:
        for cid, r in results.items():
            print(f"  {cid}: {r.count('PASS')}/{len(r)} trials passed")
    print(f"\n{passes}/{len(cases)} passed" + (f", {errors} not graded (ERROR: rerun them)" if errors else "")
          + f". Answers: {outdir}")
    sys.exit(0 if passes == len(cases) else 2 if errors else 1)


if __name__ == "__main__":
    main()
