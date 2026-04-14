import json
from pathlib import Path

STORAGE_PATH = Path.home() / ".get2work" / "data.json"

DEFAULT_DATA = {
    "commits": 0,
    "streak": 0,
    "last_commit_date": None,
    "level": 1,
    "total_lines_added": 0,
    "total_lines_deleted": 0,
    "pomodoros_completed": 0,
    "distractions_caught": 0,
}

def load() -> dict:
    if not STORAGE_PATH.exists():
        STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
        save(DEFAULT_DATA)
        return DEFAULT_DATA.copy()
    with open(STORAGE_PATH) as f:
        return json.load(f)

def save(data: dict):
    STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STORAGE_PATH, "w") as f:
        json.dump(data, f, indent=2)

def increment(key: str, amount: int = 1):
    data = load()
    data[key] = data.get(key, 0) + amount
    save(data)

def update(key: str, value):
    data = load()
    data[key] = value
    save(data)