import tempfile
from git import Repo

def clone_repo(repo_url):
    """
    Clone GitHub repo to a temporary directory
    """
    temp_dir = tempfile.mkdtemp()

    try:
        Repo.clone_from(repo_url, temp_dir, depth=1)
        return temp_dir
    except Exception as e:
        print(f"❌ Failed to clone repo: {e}")
        return None