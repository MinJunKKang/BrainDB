import json
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

SHORT_TERM_PATH = os.path.join(DATA_DIR, "short_term.json")
DEFAULT_TTL = 60

def save_to_short_term(content: str):
    now = int(time.time())
    expire_at = now + DEFAULT_TTL

    new_entry = {
        "content": content,
        "expire_at": expire_at,
        "count": 1
    }

    if os.path.exists(SHORT_TERM_PATH):
        with open(SHORT_TERM_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(new_entry)

    with open(SHORT_TERM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Saved to short-term memory: {content}")
