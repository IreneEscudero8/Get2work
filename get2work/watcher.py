import time
import random
import git
from datetime import date, datetime
from rich.console import Console
from get2work.storage import load, save, increment, update
from get2work.levels import check_levelup
from get2work.celebrate import celebrate_commit, celebrate_levelup, code_funeral, play_shame

console = Console()

SHAME_MESSAGES_LOW = [
    "hey... everything ok? no commits today 👀",
    "sooo are we coding or just vibing?",
    "the repo is lonely. just saying.",
    "no pressure but... commit something maybe?",
    "gentle reminder that you exist and so does git",
]

SHAME_MESSAGES_MED = [
    "your streak is in danger bro 😬",
    "bro really said 'i'll commit later' huh",
    "the codebase misses you. or maybe it doesn't. hard to tell.",
    "ok so we're just not committing today? ok.",
    "your github is looking a little dry rn 💀",
]

SHAME_MESSAGES_HIGH = [
    "I'M NOT MAD I'M JUST DISAPPOINTED",
    "THE AUDACITY OF NOT COMMITTING",
    "at this point are you even a developer",
    "your github is a desert. a wasteland. nothing.",
    "bro said 'i'm a developer' and then didn't develop 💀",
    "the commit history called. it's filing a missing persons report.",
]

def get_shame_message(hours_since_commit: int) -> str:
    if hours_since_commit < 4:
        return random.choice(SHAME_MESSAGES_LOW)
    elif hours_since_commit < 8:
        return random.choice(SHAME_MESSAGES_MED)
    else:
        return random.choice(SHAME_MESSAGES_HIGH)

class CommitWatcher:
    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path
        self.last_commit = None
        self._get_last_commit()

    def _get_last_commit(self):
        try:
            repo = git.Repo(self.repo_path, search_parent_directories=True)
            commits = list(repo.iter_commits(max_count=1))
            if commits:
                self.last_commit = commits[0].hexsha
        except Exception:
            pass

    def check_new_commit(self):
        try:
            repo = git.Repo(self.repo_path, search_parent_directories=True)
            commits = list(repo.iter_commits(max_count=1))
            if not commits:
                return
            latest = commits[0]
            if latest.hexsha == self.last_commit:
                return
            self.last_commit = latest.hexsha
            self._handle_new_commit(repo, latest)
        except Exception:
            pass

    def _handle_new_commit(self, repo, commit):
        try:
            stats = commit.stats.total
            lines_added = stats.get("insertions", 0)
            lines_deleted = stats.get("deletions", 0)
        except Exception:
            lines_added = 0
            lines_deleted = 0

        increment("commits")
        increment("total_lines_added", lines_added)
        increment("total_lines_deleted", lines_deleted)

        self._update_streak()
        celebrate_commit()

        if lines_deleted > 100:
            code_funeral()

        leveled_up, level_name = check_levelup()
        if leveled_up:
            celebrate_levelup(level_name)

    def _update_streak(self):
        data = load()
        today = str(date.today())
        last = data.get("last_commit_date")

        if last == today:
            return

        if last is None:
            data["streak"] = 1
        else:
            last_date = datetime.strptime(last, "%Y-%m-%d").date()
            diff = (date.today() - last_date).days
            if diff == 1:
                data["streak"] = data.get("streak", 0) + 1
            else:
                data["streak"] = 1

        data["last_commit_date"] = today
        save(data)

    def check_shame(self):
        data = load()
        last = data.get("last_commit_date")
        today = str(date.today())

        if last == today:
            console.print("\n  [bold green]✅ you committed today. we're proud.[/bold green]")
            console.print("  [dim]don't ruin it.[/dim]\n")
            return

        if last is None:
            hours = 24
        else:
            last_date = datetime.strptime(last, "%Y-%m-%d")
            hours = int((datetime.now() - last_date).total_seconds() / 3600)

        msg = get_shame_message(hours)
        play_shame()
        console.print(f"\n  [bold red]⚠️  {msg}[/bold red]\n")
            
def update_streak():
    data = load()
    today = str(date.today())
    last = data.get("last_commit_date")

    if last == today:
        return

    if last is None:
        data["streak"] = 1
    else:
        last_date = datetime.strptime(last, "%Y-%m-%d").date()
        diff = (date.today() - last_date).days
        if diff == 1:
            data["streak"] = data.get("streak", 0) + 1
        else:
            data["streak"] = 1

    data["last_commit_date"] = today
    save(data)        

def start_watching(repo_path: str = "."):
    watcher = CommitWatcher(repo_path)
    console.print("\n  [bold green]get2work is watching you 👀[/bold green]")
    console.print("  [dim]commit something or face the consequences[/dim]\n")

    check_interval = 0
    while True:
        watcher.check_new_commit()
        check_interval += 1

        if check_interval % 180 == 0:
            watcher.check_shame()

        time.sleep(10)