🚀 RepoSentry

Fast, lightweight CLI tool for security and quality analysis of code repositories.

🧭 Overview

RepoSentry is a developer-focused command-line tool that performs rapid analysis of local and GitHub repositories to identify common security risks and code quality issues.

It is designed as a first layer of defense—helping developers quickly surface high-risk patterns such as hardcoded secrets, unsafe function usage, and misconfigurations before deeper security audits.

By combining efficient file traversal, parallel processing, and rule-based detection, RepoSentry delivers actionable insights in seconds without requiring heavy setup or complex integrations.

⚙️ Key Features
🔍 Repository Scanning
Analyze both local projects and remote GitHub repositories seamlessly
🚨 Security Detection
Identify patterns like:
Hardcoded credentials
Unsafe functions (e.g., eval)
Debug configurations
Weak hashing usage
⚡ High Performance
Parallel file processing ensures fast execution even on larger codebases
📊 Project Health Score
Quantifies repository quality on a 0–100 scale
🛡 Risk Classification
Categorizes projects into:
🟢 Good
🟡 Moderate
🔴 High Risk
🧩 Modular Architecture
Easily extendable rule engine for adding custom detection logic
🚀 Installation
git clone https://github.com/PDdogra/RepoSentry.git
cd RepoSentry
pip install -r requirements.txt
💻 Usage
▶ Scan a local repository
python -m reposentry.cli .
▶ Scan a GitHub repository
python -m reposentry.cli https://github.com/psf/requests
📌 Sample Output
🔍 Input: .

📁 Scanning path: .

🚨 HIGH ISSUES:
 - Hardcoded password detected (config.py)

⚠ MEDIUM ISSUES:
 - Debug mode enabled (app.py)

📊 Total Issues: 2
📊 Score: 77/100
🛡 Risk Level: 🟡 Moderate

✔ Scan complete
🧠 How It Works

RepoSentry follows a simple but effective pipeline:

Repository Ingestion
Accepts local paths or clones GitHub repositories using shallow cloning
File Traversal
Recursively scans relevant files while excluding internal and irrelevant directories
Parallel Analysis
Applies detection rules across files using multithreading for speed
Rule-Based Detection
Identifies known insecure patterns using lightweight pattern matching
Aggregation & Scoring
Consolidates findings into severity-based output and computes a health score
🛠️ Tech Stack
Python 3
argparse — CLI interface
GitPython — GitHub integration
concurrent.futures — parallel processing
re — pattern matching
🎯 Use Cases
🔐 Quick security checks before deployment
🔎 Evaluating third-party/open-source repositories
📚 Learning and reinforcing secure coding practices
⚡ Lightweight alternative to heavy static analysis tools
⚠️ Limitations

RepoSentry is intentionally lightweight and does not replace full-scale security scanners like Bandit or SAST tools.
It is best used for early-stage detection and rapid assessments.

🧩 Future Enhancements
Custom rule configuration
JSON / report export
CI/CD integration
Language support beyond Python
👨‍💻 Author

Pranav Dogra
Cybersecurity | Developer | Builder

⭐ Final Note

RepoSentry is built with a focus on speed, clarity, and practical utility—bridging the gap between quick checks and deeper security analysis.

If you find it useful, consider ⭐ starring the repo.
