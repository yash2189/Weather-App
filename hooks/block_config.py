import sys
from pathlib import Path


def main():
    blocked_files = ["config.json"]
    found = [f for f in sys.argv[1:] if Path(f).name in blocked_files]

    if found:
        print(f"[ERROR] Blocking commit: {', '.join(found)} should not be committed.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
