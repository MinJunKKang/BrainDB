import json
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

SHORT_TERM_PATH = os.path.join(DATA_DIR, "short_term.json")
DEFAULT_TTL = 60

# 단기기억 저장
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

# 망각
def clean_expired_memory():
    now = int(time.time())
    removed = 0

    if os.path.exists(SHORT_TERM_PATH):
        with open(SHORT_TERM_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

        # 유효한 기억만 필터링
        valid_data = [item for item in data if item["expire_at"] > now]
        removed = len(data) - len(valid_data)

        with open(SHORT_TERM_PATH, "w", encoding="utf-8") as f:
            json.dump(valid_data, f, indent=4, ensure_ascii=False)

    return removed

# 인출
def search_and_update_count(keyword: str):
    now = int(time.time())
    results = []

    if not os.path.exists(SHORT_TERM_PATH):
        return results

    with open(SHORT_TERM_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    updated = False
    for item in data:
        if item["expire_at"] > now and keyword in item["content"]:
            item["count"] += 1
            item["expire_at"] = now + DEFAULT_TTL
            results.append(item)
            updated = True

    if updated:
        with open(SHORT_TERM_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    return results
