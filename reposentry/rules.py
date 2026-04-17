import re
from typing import List, Dict

def analyze_file(filepath: str) -> List[Dict]:
    """
    Analyze a file for security issues
    """
    issues = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

            # Rule 1: eval usage
            if "eval(" in content:
                issues.append({
                    "severity": "HIGH",
                    "message": "Use of eval() detected",
                    "file": filepath
                })

            # Rule 2: Hardcoded password
            if re.search(r"password\s*=\s*['\"].+['\"]", content, re.IGNORECASE):
                issues.append({
                    "severity": "HIGH",
                    "message": "Hardcoded password detected",
                    "file": filepath
                })

            # Rule 3: Debug mode
            if "debug=True" in content:
                issues.append({
                    "severity": "MEDIUM",
                    "message": "Debug mode enabled",
                    "file": filepath
                })

            # Rule 4: Weak hashing
            if "md5(" in content or "sha1(" in content:
                issues.append({
                    "severity": "MEDIUM",
                    "message": "Weak hashing algorithm used",
                    "file": filepath
                })

    except Exception:
        pass  # skip unreadable files

    return issues