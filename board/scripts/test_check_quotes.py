"""Run: python3 -I test_check_quotes.py. Regression: a quote under 20 characters shifted the pairing (found 16 Nov 2026)."""
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("cq", pathlib.Path(__file__).with_name("check_quotes.py"))
cq = importlib.util.module_from_spec(spec); spec.loader.exec_module(cq)
line = '"Supply side is 👑." (S006), so yes, an anchor shop matters. "you focus on getting 1,000 users who are densely connected already." (S115)'
got = list(cq.quotes(line))
assert got == [("you focus on getting 1,000 users who are densely connected already.", "S115")], got
print("ok")
