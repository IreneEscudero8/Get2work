import random
import requests
from rich.console import Console
from datetime import datetime, timezone

console = Console()

SARCASTIC_COMMENTS = [
    "and what are YOU doing with your life?",
    "must be nice to actually commit things 👀",
    "imagine being this productive. couldn't be you huh",
    "they said 'i'll do it later' and then did it NOW",
    "not you watching others work while you're here",
    "the dedication... the consistency... the shame you should feel",
    "ok but why are they built different tho",
    "they woke up and chose violence (against procrastination)",
    "this person has never heard of 'i'll do it tomorrow'",
    "ratio'd by someone's commit history 💀",
    "they're just like you but... productive",
    "bro said 'ship it' and actually shipped it",
]

NO_COMMITS_COMMENTS = [
    "even THEY took a day off. you have no excuse though.",
    "ok they're resting. you should be coding.",
    "slow day for them. not an excuse for you.",
]

RANDOM_USERNAMES = [
    "antfu", "patak-dev", "sxzz",
    "privatenumber", "jantimon", "nzakas",
    "ljharb", "nicolo-ribaudo", "sheremet-va",
    "yyx990803", "egoist", "pi0",
    "unjs", "Rich-Harris", "sveltejs",
]

def get_recent_commits(username: str) -> list:
    try:
        url = f"https://api.github.com/users/{username}/events/public"
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return []

        events = response.json()
        commits = []
        for event in events:
            if event.get("type") == "PushEvent":
                payload = event.get("payload", {})
                repo = event.get("repo", {}).get("name", "unknown")
                event_commits = payload.get("commits", [])
                if event_commits:
                    for commit in event_commits:
                        msg = commit.get("message", "").split("\n")[0]
                        if msg:
                            commits.append({
                                "message": msg,
                                "repo": repo,
                                "date": event.get("created_at", ""),
                            })
                else:
                    commits.append({
                        "message": "pushed some code 👀",
                        "repo": repo,
                        "date": event.get("created_at", ""),
                    })
            if len(commits) >= 5:
                break
        return commits

    except Exception:
        return []
    
def format_time_ago(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        diff = now - dt
        minutes = int(diff.total_seconds() / 60)

        if minutes < 60:
            return f"{minutes}m ago"
        elif minutes < 1440:
            return f"{minutes // 60}h ago"
        else:
            return f"{minutes // 1440}d ago"
    except Exception:
        return "recently"

def _display_commits(username: str, commits: list):
    if not commits:
        comment = random.choice(NO_COMMITS_COMMENTS)
        console.print(f"  [dim]no recent commits from {username}[/dim]")
        console.print(f"  [yellow]👀 {comment}[/yellow]\n")
        return

    comment = random.choice(SARCASTIC_COMMENTS)
    console.print(f"  [bold]recent commits by [cyan]{username}[/cyan]:[/bold]\n")

    for c in commits:
        time_ago = format_time_ago(c["date"])
        console.print(f"  [green]▸[/green] [white]{c['message']}[/white]")
        console.print(f"    [dim]{c['repo']} · {time_ago}[/dim]")

    console.print(f"\n  [bold yellow]👀 {comment}[/bold yellow]\n")

def peer_pressure(username: str):
    console.print(f"\n  [bold cyan]checking what {username} is up to...[/bold cyan]\n")
    commits = get_recent_commits(username)
    _display_commits(username, commits)

def random_peer():
    console.print(f"\n  [bold magenta]pulling a random dev from the void...[/bold magenta]\n")
    
    usernames = random.sample(RANDOM_USERNAMES, len(RANDOM_USERNAMES))
    
    for username in usernames:
        commits = get_recent_commits(username)
        if commits:
            _display_commits(username, commits)
            return

    console.print("  [dim]all devs are slacking too. rare.[/dim]")
    console.print("  [yellow]👀 even the internet is taking a break. no excuses for you though.[/yellow]\n")