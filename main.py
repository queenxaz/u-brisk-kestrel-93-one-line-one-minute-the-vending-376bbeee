import os

LINE = "Hey Judge, I’m the vending machine: press B7 and I’ll drop something sweet, because you’re the only human who never shakes me."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# The entry line is fixed and deterministic; see README.md for the text.
