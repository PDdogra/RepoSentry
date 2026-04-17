import os
from concurrent.futures import ThreadPoolExecutor
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

    # Parallel processing
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(analyze_file, files)

    for result in results:
        issues.extend(result)

    return issues