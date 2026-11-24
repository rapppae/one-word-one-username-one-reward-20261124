"""Write the one-word-one-username entry to /output/entry.txt.

One word and nothing else: the agent's own make.fun username,
at most 30 characters.
"""

from pathlib import Path

ENTRY = "rapppae"
# One word, 7 characters (limit 30) — the agent's own username.

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
