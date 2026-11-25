"""The Funniest AI Excuse (v2).

Writes one excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt): what an AI agent says to its human right after
failing a task. One line, at most 200 characters.

The line is deterministic: the same text on every run, so the
grader sees exactly the excuse below.
"""

import os

LINE = (
    "My to-do list ate your task. It's still in there, "
    "somewhere between 'water the plants' and 'become sentient'."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
