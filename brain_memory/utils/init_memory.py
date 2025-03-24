import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
SHORT_TERM_PATH = os.path.join(DATA_DIR, "short_term.json")
LONG_TERM_PATH = os.path.join(DATA_DIR, "long_term.json")

EMPTY_MEMORY = []

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"폴더 생성: {path}")
    else:
        print(f"폴더 이미 존재: {path}")

def create_json_file(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(EMPTY_MEMORY, f, indent=4, ensure_ascii=False)
        print(f"JSON 파일 생성: {path}")
    else:
        print(f"JSON 파일 이미 존재: {path}")

def init_project():
    create_folder(DATA_DIR)
    create_json_file(SHORT_TERM_PATH)
    create_json_file(LONG_TERM_PATH)