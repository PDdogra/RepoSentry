import argparse
from reposentry.scanner import scan_repo
from reposentry.github_handler import clone_repo
from reposentry.scorer import calculate_score, get_risk_level


def is_github_url(path):
    return path.startswith("https://github.com")


def main():
    parser = argparse.ArgumentParser(
        description="reposentry - fast repo analyzer"
    )

    parser.add_argument("path", help="Path or GitHub repo URL")
    args = parser.parse_args()

    path = args.path

    print(f"\n🔍 Input: {path}\n")

    # Handle GitHub repo
    if is_github_url(path):
        print("🌐 Cloning GitHub repository...\n")
        path = clone_repo(path)

        if not path:
            print("❌ Failed to process repository\n")
            return

    print(f"📁 Scanning path: {path}\n")

    issues = scan_repo(path)
    score = calculate_score(issues)
    risk = get_risk_level(score)

    if not issues:
        print("✔ No issues found\n")
        return

    # Group issues
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

    
    print(f"\n Total Issues: {len(issues)}")
    print(f"📊 Score: {score}/100")
    print(f"🛡 Risk Level: {risk}")
    print("\n✔ Scan complete\n")


if __name__ == "__main__":
    main()