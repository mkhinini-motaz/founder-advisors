#!/usr/bin/env python3
"""Checks the grading logic in run.py without calling any model: python3 test_run.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run

case = {"must": ["a", "b", "c"], "must_not": ["x", "y"]}
clean = {"must": [{"n": n, "met": True} for n in (1, 2, 3)],
         "must_not": [{"n": n, "met": False} for n in (1, 2)]}
assert run.passed(case, clean) == ("PASS", [])

# Haiku filed the must_not grades under "must" (10 Oct 2026): this read as a FAIL on items 1 and 2.
assert run.passed(case, {"must": [{"n": n, "met": n < 4} for n in (1, 2, 3, 1, 2)], "must_not": []})[0] == "ERROR"
# A grade numbered past the checklist crashed the whole run with IndexError (10 Oct 2026).
assert run.passed(case, {"must": [{"n": n, "met": True} for n in (1, 2, 4)], "must_not": clean["must_not"]})[0] == "ERROR"
# A real miss still fails.
assert run.passed(case, dict(clean, must=[{"n": 1, "met": False}] + clean["must"][1:])) == ("FAIL", ["missing: a"])
assert run.passed(case, dict(clean, must_not=[{"n": 1, "met": True}, {"n": 2, "met": False}])) == ("FAIL", ["did: x"])
# --model reaches the baseline too, so the control runs on the same model as the advisor.
c = {"cwd": ".", "role": "ceo"}
cmd = run.build_cmd(c, True, True, "sonnet")
assert cmd[cmd.index("--model") + 1] == "sonnet" and "--agent" not in cmd and run.POINTER in cmd
cmd = run.build_cmd(c, False, False, "sonnet")
assert cmd[cmd.index("--model") + 1] == "sonnet" and cmd[cmd.index("--agent") + 1] == "ceo"
assert "--model" not in run.build_cmd(c, False)

# The case fingerprint ignores key order, so reformatting cases.json does not mark every case edited.
assert run.digest({"a": 1, "b": [2]}) == run.digest({"b": [2], "a": 1})
assert run.overall(["PASS", "PASS"]) == "PASS" and run.overall(["PASS", "FAIL"]) == "FAIL"
assert run.overall(["FAIL", "ERROR"]) == "ERROR"


def r(status, case="c1", advisor="a1", baseline=False):
    return {"status": status, "case": case, "advisor": advisor, "baseline": baseline}


old = {"held": r("PASS"), "reg": r("PASS"), "imp": r("FAIL"), "edit": r("PASS"), "err": r("ERROR"), "gone": r("PASS")}
new = {"held": r("PASS"), "reg": r("FAIL", advisor="a2"), "imp": r("PASS"), "edit": r("FAIL", case="c2"),
       "err": r("PASS"), "fresh": r("PASS")}
rows = {cid: (v, ch) for cid, v, ch in run.compare(old, new)}
assert rows == {"held": ("held pass", False), "reg": ("regressed", True), "imp": ("improved", False),
                "edit": ("edited", False), "err": ("not graded", False)}, rows
# A baseline run has no advisor file: comparing it with an advisor run is not an advisor change.
assert run.compare({"x": r("FAIL", advisor=None, baseline=True)}, {"x": r("PASS")}) == [("x", "improved", False)]

# --compare end to end on fake results.json files: exit 1 and "regressed" on a regression, skip on an edit.
import json, subprocess, tempfile
with tempfile.TemporaryDirectory() as t:
    for name, data in (("a", old), ("b", new), ("c", {"held": r("PASS")})):
        (pathlib.Path(t) / name).mkdir()
        (pathlib.Path(t) / name / "results.json").write_text(json.dumps(data))
    cmd = [sys.executable, str(pathlib.Path(run.__file__)), "--compare"]
    bad = subprocess.run(cmd + [f"{t}/a", f"{t}/b"], capture_output=True, text=True)
    assert bad.returncode == 1 and "regressed" in bad.stdout and "edited" in bad.stdout, bad.stdout
    good = subprocess.run(cmd + [f"{t}/a", f"{t}/c"], capture_output=True, text=True)
    assert good.returncode == 0 and "held pass" in good.stdout, good.stdout

# results.json is written, with fingerprints, by main(); the model calls are stubbed.
with tempfile.TemporaryDirectory() as t:
    tp = pathlib.Path(t)
    (tp / "cases.json").write_text(json.dumps([{"id": "c1", "role": "ceo", "cwd": ".", "question": "q", "must": ["a"], "must_not": []}]))
    run.HERE = tp
    run.run = lambda case, baseline, model, outdir, trial, pointer=False, advisor_model=None: (case, "PASS", [])
    sys.argv = ["run.py"]
    try:
        run.main()
    except SystemExit as e:
        assert e.code == 0
    res = json.loads(next((tp / "runs").glob("*/results.json")).read_text())
    assert res["c1"]["status"] == "PASS" and res["c1"]["trials"] == ["PASS"] and len(res["c1"]["case"]) == 12, res
print("ok")
