import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FOLDERS = [
    os.path.join(BASE_DIR, "data"),
    os.path.join(BASE_DIR, "gui"),
    os.path.join(BASE_DIR, "utils")
]

SHORT_TERM_FILE = os.path.join(BASE_DIR, "data", "short_term.json")
LONG_TERM_FILE = os.path.join(BASE_DIR, "data", "long_term.json")

empty_memory = []

def create_folders():
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok = True)

def create_json_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(empty_memory, f, indent=4)
        print(f" Created: {file_path}")
    else:
        print(f"Already exists: {file_path}")

def init_project():
    create_folders()
    create_json_file(SHORT_TERM_FILE)
    create_json_file(LONG_TERM_FILE)

if __name__ == "__main__":
    init_project()