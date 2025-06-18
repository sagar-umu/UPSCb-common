import os
import shutil

REPO_ROOT = "."
DOCS_DIR = "docs"

EXCLUDE_DIRS = {
    DOCS_DIR, ".git", ".github", "__pycache__", "site", "venv", ".venv", ".mypy_cache"
}
EXCLUDE_FILES = {
    "mkdocs.yml", "requirements.txt", "readthedocs.yml", "clone_directories_to_docs.py"
}

def should_copy(src, dst):
    """Returns True if dst does not exist or src is newer."""
    return not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)

def safe_copytree(src, dst):
    """Copies files from src to dst, updating .md files only if changed."""
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)

        if os.path.isdir(src_item):
            safe_copytree(src_item, dst_item)
        elif os.path.isfile(src_item):
            if item.endswith(".md"):
                if should_copy(src_item, dst_item):
                    shutil.copy2(src_item, dst_item)
                    print(f"Updated .md file: {src_item} -> {dst_item}")
                else:
                    print(f"Skipped unchanged .md: {dst_item}")
            else:
                shutil.copy2(src_item, dst_item)
                print(f"Copied: {src_item} -> {dst_item}")

def clone_repo_dirs():
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)

    for entry in os.listdir(REPO_ROOT):
        src_path = os.path.join(REPO_ROOT, entry)
        dst_path = os.path.join(DOCS_DIR, entry)

        if entry in EXCLUDE_DIRS or entry in EXCLUDE_FILES or entry.startswith("."):
            continue

        if os.path.isdir(src_path):
            print(f"Cloning folder: {entry}")
            safe_copytree(src_path, dst_path)
        elif os.path.isfile(src_path) and entry.endswith(".md"):
            dst_file = os.path.join(DOCS_DIR, entry)
            if should_copy(src_path, dst_file):
                shutil.copy2(src_path, dst_file)
                print(f"Updated root .md file: {entry}")
            else:
                print(f"Skipped unchanged root .md: {entry}")

if __name__ == "__main__":
    clone_repo_dirs()
