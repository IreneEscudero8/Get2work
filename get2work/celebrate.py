import time
import random
import os
from pathlib import Path
from rich.console import Console

console = Console()

SOUNDS_DIR = Path(__file__).parent / "sounds"

CUSTOM_SOUNDS = {
    "celebrate": os.environ.get("GET2WORK_SOUND_CELEBRATE"),
    "funeral": os.environ.get("GET2WORK_SOUND_FUNERAL"),
    "shame": os.environ.get("GET2WORK_SOUND_SHAME"),
    "levelup": os.environ.get("GET2WORK_SOUND_LEVELUP"),
    "success": os.environ.get("GET2WORK_SOUND_SUCCESS"),
    "error": os.environ.get("GET2WORK_SOUND_ERROR"),
}

DEFAULT_SOUNDS = {
    "celebrate": SOUNDS_DIR / "celebrate.mp3",
    "funeral":   SOUNDS_DIR / "funeral.mp3",
    "shame":     SOUNDS_DIR / "shame.mp3",
    "levelup":   SOUNDS_DIR / "levelup.mp3",
    "success":   SOUNDS_DIR / "success.mp3",
    "error":     SOUNDS_DIR / "error.mp3",
}

COMMIT_MESSAGES = [
    "YOOOO YOU ACTUALLY COMMITTED 🔥",
    "look at you being productive omg",
    "a commit?? in THIS economy??",
    "slay bestie, that's a commit",
    "the git history thanks you",
    "ok ok ok we're doing this 💪",
    "committed and not quitting, respect",
    "your future self says thanks... maybe",
]

LEVELUP_MESSAGES = [
    "YOU LEVELED UP ARE YOU KIDDING ME",
    "bro is actually getting good at this",
    "the grindset is REAL",
    "level up achieved, touch grass later",
    "ok we are NOT the same anymore 👑",
]

FUNERAL_MESSAGES = [
    "rip to those lines of code 💀",
    "they didn't make it...",
    "gone but not forgotten (they were probably bad anyway)",
    "a moment of silence for your deleted code",
    "the codebase is lighter now. emotionally too.",
]

def play_sound(name: str):
    try:
        import pygame
        custom = CUSTOM_SOUNDS.get(name)
        path = Path(custom) if custom else DEFAULT_SOUNDS.get(name)

        if not path or not path.exists():
            return

        pygame.mixer.init()
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play()
        time.sleep(1.5)
        pygame.mixer.quit()
    except Exception:
        pass

def celebrate_commit():
    colors = ["red", "yellow", "green", "cyan", "magenta", "blue"]
    msg = random.choice(COMMIT_MESSAGES)

    play_sound("celebrate")
    console.print()
    for i in range(3):
        color = random.choice(colors)
        console.print(f"  {'🎉' * (i+2)}  {msg}  {'🎉' * (i+2)}", style=f"bold {color}")
        time.sleep(0.15)
    console.print()

def celebrate_levelup(level_name: str):
    msg = random.choice(LEVELUP_MESSAGES)

    play_sound("levelup")
    console.print()
    console.rule("[bold yellow]LEVEL UP[/bold yellow]")
    console.print(f"\n  ⚡ [bold yellow]{msg}[/bold yellow]")
    console.print(f"  👑 [bold cyan]You are now: {level_name}[/bold cyan]\n")
    console.rule("[bold yellow]LEVEL UP[/bold yellow]")
    console.print()

def code_funeral():
    msg = random.choice(FUNERAL_MESSAGES)

    play_sound("funeral")
    console.print()
    console.rule("[bold red]💀 CODE FUNERAL 💀[/bold red]")
    console.print(f"\n  [bold red]{msg}[/bold red]")
    console.print("  [dim]deleted: yes. missed: debatable.[/dim]\n")
    console.rule("[bold red]💀 💀 💀[/bold red]")
    console.print()

def play_success():
    play_sound("success")

def play_error():
    play_sound("error")

def play_shame():
    play_sound("shame")