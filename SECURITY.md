# Security

## Report a vulnerability

- Open the **Security** tab of this repository and choose **Report a vulnerability**. The report stays private.
- If that button is missing, open an issue titled "Security contact" with no details. The maintainer will reply and arrange a private channel.

Do not post details, tokens or proof-of-concept output in a public issue.

## In scope

- Your company brief: any file, script or prompt that sends it, or text taken from it, anywhere but your own agent session.
- A knowledge file or seat that holds private data about a person.
- A script in `tools/` or `evals/` (`fetch.py` reaches the network) that runs unexpected commands or writes outside the repo.

## Out of scope

- Findings that need you to run code you wrote yourself.
- Weaknesses in Claude Code, Node, Python or GitHub themselves. Report those to their owners.
