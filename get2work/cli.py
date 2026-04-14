import typer
from rich.console import Console
from datetime import date

app = typer.Typer(help="get2work — stop scrolling, start coding")
console = Console()

@app.command()
def install():
    """Install get2work hook in your repo 🔧"""
    import os
    import stat
    from pathlib import Path

    try:
        import git
        repo = git.Repo(".", search_parent_directories=True)
        hooks_dir = Path(repo.git_dir) / "hooks"
        hook_path = hooks_dir / "post-commit"

        hook_script = """#!/bin/sh
get2work celebrate-commit
"""
        with open(hook_path, "w") as f:
            f.write(hook_script)

        st = os.stat(hook_path)
        os.chmod(hook_path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

        console.print("\n  [bold green]✅ get2work installed![/bold green]")
        console.print("  [dim]now every commit will be celebrated 🎉[/dim]\n")

    except Exception as e:
        console.print(f"\n  [bold red]❌ error: {e}[/bold red]\n")

@app.command()
def celebrate_commit():
    """Triggered automatically on commit 🎉"""
    from get2work.storage import load, increment
    from get2work.levels import check_levelup
    from get2work.celebrate import celebrate_commit as do_celebrate, celebrate_levelup, code_funeral
    import git

    try:
        repo = git.Repo(".", search_parent_directories=True)
        commits = list(repo.iter_commits(max_count=1))
        if commits:
            commit = commits[0]
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

            from get2work.watcher import update_streak
            update_streak()

            do_celebrate()

            if lines_deleted > 100:
                code_funeral()

            leveled_up, level_name = check_levelup()
            if leveled_up:
                celebrate_levelup(level_name)

    except Exception as e:
        pass

@app.command()
def status():
    """Check your level, streak and stats"""
    from get2work.storage import load
    from get2work.levels import get_level, get_next_level

    data = load()
    commits = data["commits"]
    streak = data["streak"]
    level_num, level_name = get_level(commits)
    next_level = get_next_level(commits)

    console.print()
    console.rule("[bold cyan]get2work[/bold cyan]")
    console.print(f"\n  👾 [bold cyan]Level {level_num}[/bold cyan] — [yellow]{level_name}[/yellow]")
    console.print(f"  🔥 [bold]Streak:[/bold] {streak} days")
    console.print(f"  📦 [bold]Total commits:[/bold] {commits}")
    console.print(f"  🍅 [bold]Pomodoros:[/bold] {data['pomodoros_completed']}")
    console.print(f"  👀 [bold]Distractions caught:[/bold] {data['distractions_caught']}")

    if next_level:
        needed = next_level[0] - commits
        console.print(f"\n  ⚡ [dim]{needed} commits until [bold]{next_level[1]}[/bold][/dim]")

    console.print()

@app.command()
def roast():
    """Get your commits roasted 🔥"""
    from get2work.roast import roast_my_commits
    roast_my_commits()
    
@app.command()
def blame():
    """Git blame but make it personal 🔍"""
    from get2work.roast import git_blame_personal
    git_blame_personal()    

@app.command()
def vibe():
    """Get a mental health diagnosis based on your commits 🧠"""
    from get2work.roast import vibe_check
    vibe_check()
    
@app.command()
def peer(username: str = typer.Argument(..., help="GitHub username to stalk 👀")):
    """See what others are committing and feel bad about yourself 👀"""
    from get2work.peer_pressure import peer_pressure
    peer_pressure(username)    
    
@app.command()
def randompeer():
    """Get shamed by a random dev from the internet 🎲"""
    from get2work.peer_pressure import random_peer
    random_peer()
    
@app.command()
def distraction():
    """Check if you're slacking right now 👀"""
    from get2work.distraction import distraction_check
    caught = distraction_check()
    if not caught:
        console.print("\n  [bold green]✅ no distractions detected[/bold green]")
        console.print("  [dim]surprisingly productive. respect.[/dim]\n")
        
        
@app.command()
def shame():
    """Check if you deserve to be shamed right now 😤"""
    from get2work.watcher import CommitWatcher
    watcher = CommitWatcher()
    watcher.check_shame()

@app.command()
def start():
    """Start get2work in background — watches commits and distractions 👀"""
    import threading
    import time
    from get2work.watcher import CommitWatcher
    from get2work.distraction import start_distraction_watcher

    console.print("\n  [bold green]get2work is watching you 👀[/bold green]")
    console.print("  [dim]commit something or face the consequences[/dim]\n")

    watcher = CommitWatcher()

    def shame_loop():
        while True:
            time.sleep(60 * 30)
            watcher.check_shame()

    def distraction_loop():
        start_distraction_watcher(interval_seconds=120)

    t1 = threading.Thread(target=shame_loop, daemon=True)
    t2 = threading.Thread(target=distraction_loop, daemon=True)
    t1.start()
    t2.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n  [dim]get2work stopped. go touch grass.[/dim]\n")  
        
@app.command()
def pomodoro(minutes: int = typer.Option(25, help="Pomodoro duration in minutes")):
    """Start a pomodoro timer 🍅"""
    import time
    from get2work.storage import increment

    console.print(f"\n  🍅 [bold green]Pomodoro started — {minutes} minutes[/bold green]")
    console.print("  [dim]focus mode activated, no excuses[/dim]\n")

    total_seconds = minutes * 60
    with console.status("[green]working...[/green]") as status:
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            status.update(f"[green]⏱ {mins:02d}:{secs:02d} remaining — stay focused[/green]")
            time.sleep(1)

    increment("pomodoros_completed")
    console.print("\n  ✅ [bold green]POMODORO DONE![/bold green]")
    console.print("  [dim]ok now you can touch grass for 5 minutes[/dim]\n")

@app.command()
def receipt():
    """Get your accountability receipt for today 🧾"""
    from get2work.storage import load
    from get2work.levels import get_level
    import datetime

    data = load()
    now = datetime.datetime.now()
    level_num, level_name = get_level(data["commits"])

    console.print()
    console.rule("[bold white]🧾 ACCOUNTABILITY RECEIPT[/bold white]")
    console.print(f"  [dim]{now.strftime('%Y-%m-%d %H:%M')}[/dim]\n")
    console.print(f"  Level:          {level_name}")
    console.print(f"  Commits:        {data['commits']}")
    console.print(f"  Streak:         {data['streak']} days")
    console.print(f"  Pomodoros:      {data['pomodoros_completed']}")
    console.print(f"  Distractions:   {data['distractions_caught']}")
    console.print(f"\n  [dim]Lines added:    {data['total_lines_added']}[/dim]")
    console.print(f"  [dim]Lines deleted:  {data['total_lines_deleted']}[/dim]")
    console.print()
    console.rule("[bold white]thanks for coming to get2work[/bold white]")
    console.print()

if __name__ == "__main__":
    app()