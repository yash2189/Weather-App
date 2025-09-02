import sys


def main():
    for file in sys.argv[1:]:
        with open(file) as f:
            lines = f.readlines()

        user_lines = [
            line.strip().lower()
            for line in lines
            if line.strip().lower().startswith("user")
        ]

        if not user_lines:
            print(f"{file}: No USER specified (defaults to root)")
            return 1
        if any("user root" in line for line in user_lines):
            print(f"{file}: USER root is not allowed")
            return 1

        print(f"{file}: Non-root user used")
    return 0


if __name__ == "__main__":
    sys.exit(main())
