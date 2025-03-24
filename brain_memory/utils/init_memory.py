import os
import json

folders = [
    "data",
    "gui",
    "utils"
]

short_term_file = "data/short_term.json"
long_term_file = "data/long_term.json"

empty_memory = []

def create_folders():
    for folder in folders:
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
    create_json_file(short_term_file)
    create_json_file(long_term_file)

if __name__ == "__main__":
    init_project()