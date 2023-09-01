import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(description="Do something")
    parser.add_argument("url", help="The problem url")
    parser.add_argument("-l", "--language", help="choose problem language")
    args = parser.parse_args()

    if args.language is None:
        print("Choose a language for your solution:")
        print("1. Python")
        print("2. JavaScript")
        print("3. Java")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            args.language = "python"
        elif choice == "2":
            args.language = "javascript"
        elif choice == "3":
            args.language = "java"
        else:
            print("Invalid choice. Please select a valid language.")
            return

    subprocess.run(["python", "script.py", args.url, args.language])


if __name__ == "__main__":
    main()
