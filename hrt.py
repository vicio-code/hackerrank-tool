import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(description="Do something")
    parser.add_argument("url", help="The problem url")
    args = parser.parse_args()
    subprocess.run(["python", "script.py", args.url])


if __name__ == "__main__":
    main()
