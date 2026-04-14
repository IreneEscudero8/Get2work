import psutil
import random
from rich.console import Console
from get2work.storage import increment
from get2work.celebrate import play_shame

console = Console()

DISTRACTING_APPS = [
    "netflix", "spotify", "discord", "telegram",
    "whatsapp", "instagram", "tiktok", "youtube",
    "twitch", "steam", "epicgames", "roblox",
    "minecraft", "fortnite", "chess", "solitaire",
    "slack",  "zoom", "teams",
]

DISTRACTING_URLS_KEYWORDS = [
    "youtube", "netflix", "twitter", "instagram",
    "tiktok", "reddit", "facebook", "twitch",
    "memes", "buzzfeed", "9gag",
]

CAUGHT_MESSAGES = [
    "bro really said 'just 5 minutes' 💀",
    "the audacity. the AUDACITY.",
    "we saw that. get back to work.",
    "not you watching {app} instead of coding",
    "your commits are not going to write themselves",
    "caught in 4k. close it.",
    "{app}?? really?? RIGHT NOW??",
    "the repo is crying. {app} can wait.",
    "ok so we're doing THIS instead of shipping features",
    "distraction detected. shame incoming. 🚨",
]

def get_running_processes() -> list:
    processes = []
    try:
        for proc in psutil.process_iter(['name']):
            try:
                name = proc.info['name'].lower()
                processes.append(name)
            except Exception:
                pass
    except Exception:
        pass
    return processes

def check_distractions() -> str | None:
    processes = get_running_processes()
    for proc in processes:
        for app in DISTRACTING_APPS:
            if app in proc:
                return app
    return None

def distraction_check():
    caught = check_distractions()
    if caught:
        increment("distractions_caught")
        play_shame()

        msg = random.choice(CAUGHT_MESSAGES).replace("{app}", caught)
        console.print(f"\n  [bold red]🚨 DISTRACTION DETECTED[/bold red]")
        console.print(f"  [red]{msg}[/red]\n")
        return True
    return False

def start_distraction_watcher(interval_seconds: int = 120):
    import time
    console.print("  [dim]distraction detector active 👀[/dim]")
    while True:
        distraction_check()
        time.sleep(interval_seconds)