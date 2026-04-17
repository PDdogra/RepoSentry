import argparse

def main():
    parser = argparse.ArgumentParser(
        description="reposentry - fast repo analyzer"
    )

    parser.add_argument("path", help="Path or GitHub repo URL")

    args = parser.parse_args()

    print(f"\n🔍 Scanning: {args.path}\n")

if __name__ == "__main__":
    main()