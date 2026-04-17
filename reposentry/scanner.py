import os
from reposentry.rules import analyze_file


def get_python_files(path):
    python_files = []

    for root, dirs, files in os.walk(path):

        # Skip unwanted directories
        skip_dirs = {"reposentry", "__pycache__", ".git", "venv", "env"}
        if any(skip in root for skip in skip_dirs):
            continue

        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                python_files.append(full_path)

    return python_files


def scan_repo(path):
    issues = []
    files = get_python_files(path)

    for file in files:
        file_issues = analyze_file(file)
        issues.extend(file_issues)

    return issues