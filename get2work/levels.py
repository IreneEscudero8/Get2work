from get2work.storage import load, save

LEVELS = [
    (0,   "Hello World Survivor"),
    (10,  "Tutorial Finisher"),
    (30,  "Functional but Confused"),
    (60,  "It Works Don't Touch It"),
    (100, "Commits with Confidence (wrongly)"),
    (200, "git push --force and it worked"),
    (400, "The Last Line of Defense"),
    (700, "Linus Would Be Proud"),
]

def get_level(commits: int) -> tuple:
    current = (1, LEVELS[0][1])
    for i, (threshold, name) in enumerate(LEVELS):
        if commits >= threshold:
            current = (i + 1, name)
    return current

def get_next_level(commits: int) -> tuple | None:
    for threshold, name in LEVELS:
        if commits < threshold:
            return (threshold, name)
    return None

def check_levelup() -> tuple:
    data = load()
    commits = data["commits"]
    level_num, level_name = get_level(commits)
    old_level = data.get("level", 1)

    if level_num > old_level:
        data["level"] = level_num
        save(data)
        return True, level_name
    return False, level_name