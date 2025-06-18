import os
import shutil

REPO_ROOT = "."
DOCS_DIR = "docs"

EXCLUDE_DIRS = {
    DOCS_DIR, ".git", ".github", "site", "venv", ".venv", "__pycache__", ".mypy_cache"
}
EXCLUDE_FILES = {
    "mkdocs.yml", "requirements.txt", "readthedocs.yml", "clone_directories_to_docs.py"
}

def should_copy(src, dst):
    """Copy if file doesn't exist or has been modified."""
    return not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)

def capitalize_path(path):
    """Capitalize the first component of a relative path."""
    parts = path.strip(os.sep).split(os.sep)
    return os.path.join(*[parts[0].capitalize()] + parts[1:]) if parts else path

def safe_copytree(src, dst):
    """Recursively copy directory, capitalizing folder names and smart-updating .md files."""
    for root, dirs, files in os.walk(src):
        rel_path = os.path.relpath(root, src)
        capitalized_path = capitalize_path(rel_path)
        dst_root = os.path.join(dst, capitalized_path) if rel_path != '.' else dst

        os.makedirs(dst_root, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_root, file)

            if file.endswith(".md"):
                if should_copy(src_file, dst_file):
                    shutil.copy2(src_file, dst_file)
                    print(f"Updated .md file: {dst_file}")
                else:
                    print(f"Skipped unchanged .md: {dst_file}")
            else:
                shutil.copy2(src_file, dst_file)
                print(f"Copied file: {dst_file}")

def clone_repo_dirs():
    os.makedirs(DOCS_DIR, exist_ok=True)

    for entry in os.listdir(REPO_ROOT):
        src_path = os.path.join(REPO_ROOT, entry)
        cap_entry = entry.capitalize()
        dst_path = os.path.join(DOCS_DIR, cap_entry)

        if entry in EXCLUDE_DIRS or entry in EXCLUDE_FILES or entry.startswith("."):
            continue

        if os.path.isdir(src_path):
            print(f"Cloning folder: {entry} -> {cap_entry}/")
            safe_copytree(src_path, dst_path)
        elif os.path.isfile(src_path) and entry.endswith(".md"):
            dst_file = os.path.join(DOCS_DIR, cap_entry)
            if should_copy(src_path, dst_file):
                shutil.copy2(src_path, dst_file)
                print(f"Copied root .md file: {entry}")
            else:
                print(f"Skipped unchanged root .md: {entry}")

if __name__ == "__main__":
    clone_repo_dirs()
