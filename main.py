# main.py
import clone_directories_to_docs

def define_env(env):
    @env.macro
    def prepare_docs():
        clone_directories_to_docs.clone_repo_dirs()
