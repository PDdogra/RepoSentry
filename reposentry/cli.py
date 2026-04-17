import argparse
from reposentry.scanner import scan_repo


def main():
    parser = argparse.ArgumentParser(
        description="reposentry - fast repo analyzer"
    )

    parser.add_argument("path", help="Path or GitHub repo URL")
    args = parser.parse_args()

    print(f"\n🔍 Scanning: {args.path}\n")

    issues = scan_repo(args.path)

    if not issues:
        print("✔ No issues found\n")
        return

    # Group issues by severity
    high = [i for i in issues if i["severity"] == "HIGH"]
    medium = [i for i in issues if i["severity"] == "MEDIUM"]

    if high:
        print("🚨 HIGH ISSUES:")
        for i in high:
            print(f" - {i['message']} ({i['file']})")

    if medium:
        print("\n⚠ MEDIUM ISSUES:")
        for i in medium:
            print(f" - {i['message']} ({i['file']})")

    print(f"\n📊 Total Issues: {len(issues)}\n")
    print("✔ Scan complete\n")


if __name__ == "__main__":
    main()