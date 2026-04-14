import random
from rich.console import Console

console = Console()

ROAST_FALLBACK = [
    "your commits look like you're coding with your eyes closed ngl",
    "bro really said 'fix' 5 times in a row. fix WHAT??",
    "committing at 3am again? the grindset is NOT it",
    "your commit history reads like a cry for help",
    "one commit today? one? really? ok.",
    "the way you commit... your tech lead is losing sleep",
    "'update' is not a commit message. try again bestie",
    "your streak died and you didn't even notice 💀",
    "bro codes like they're defusing a bomb at all times",
    "the git log called. it's concerned about you.",
]

VIBE_FALLBACK = [
    "diagnosis: you're cooked but in a productive way",
    "your commits say 'i am fine' but the timestamps say otherwise",
    "clinical assessment: chaotic good developer with trust issues",
    "you commit like someone who has seen things. dark things.",
    "prognosis: will survive, but the codebase might not",
    "your vibe is 'senior dev in a junior's body' and it shows",
    "mental state: 404 work life balance not found",
    "you're not burnout, you're just... extra crispy",
]

def get_commits_summary(repo_path: str = ".") -> str:
    try:
        import git
        repo = git.Repo(repo_path, search_parent_directories=True)
        commits = list(repo.iter_commits(max_count=20))
        if not commits:
            return "No commits found"
        summary = []
        for c in commits:
            summary.append(f"- {c.message.strip()} ({c.authored_datetime.strftime('%A %H:%M')})")
        return "\n".join(summary)
    except Exception as e:
        return f"Error reading commits: {e}"

def _try_ai_roast(commits_summary: str, mode: str = "roast") -> str | None:
    try:
        from openai import OpenAI
        import os

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return None

        client = OpenAI(api_key=api_key)

        if mode == "roast":
            system = """You are a savage but funny code roaster.
Roast the developer based on their git commit history.
Be sarcastic, funny and gen z. Max 4 lines.
Respond in the same language the commits are written in."""
        else:
            system = """You are a therapist for developers but make it sarcastic.
Analyze the git commit history and give a mental health diagnosis.
Be funny, gen z, and dramatic. Max 5 lines.
Respond in the same language the commits are written in."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=300,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": f"Commits:\n{commits_summary}"}
            ]
        )
        return response.choices[0].message.content

    except Exception:
        return None

def roast_my_commits(repo_path: str = "."):
    console.print("\n  [bold magenta]loading your L's...[/bold magenta]\n")
    commits = get_commits_summary(repo_path)

    result = _try_ai_roast(commits, mode="roast")
    source = "🤖 AI ROAST" if result else "🔥 ROAST"
    if not result:
        result = random.choice(ROAST_FALLBACK)

    console.print(f"  [bold red]{source}:[/bold red]\n")
    console.print(f"  [red]{result}[/red]\n")

def vibe_check(repo_path: str = "."):
    console.print("\n  [bold cyan]analyzing your vibe...[/bold cyan]\n")
    commits = get_commits_summary(repo_path)

    result = _try_ai_roast(commits, mode="vibe")
    source = "🤖 AI VIBE CHECK" if result else "🧠 VIBE CHECK"
    if not result:
        result = random.choice(VIBE_FALLBACK)

    console.print(f"  [bold cyan]{source}:[/bold cyan]\n")
    console.print(f"  [cyan]{result}[/cyan]\n")
    
BLAME_FALLBACK = [
    "this line was written by someone who had given up on life",
    "whoever wrote this was clearly having a bad day. we don't judge. we do judge.",
    "this code works and nobody knows why. not even the author.",
    "written at 2am. you can tell.",
    "the author of this line has since left the company. smart move.",
    "this is either genius or a cry for help. probably both.",
    "no comment. literally, they left no comment. typical.",
    "the person who wrote this knew exactly what they were doing. unfortunately.",
    "this line has survived 3 refactors. it's unkillable. it's a cockroach.",
    "written with the confidence of someone who doesn't have to maintain this.",
]

def git_blame_personal(repo_path: str = "."):
    import git

    console.print("\n  [bold yellow]analyzing who to blame...[/bold yellow]\n")

    try:
        repo = git.Repo(repo_path, search_parent_directories=True)
        commits = list(repo.iter_commits(max_count=10))

        if not commits:
            console.print("  [dim]no commits to blame. you're safe. for now.[/dim]\n")
            return

        blame_data = []
        for commit in commits[:5]:
            blame_data.append({
                "author": commit.author.name,
                "message": commit.message.strip().split("\n")[0],
                "date": commit.authored_datetime.strftime("%A %H:%M"),
                "files": list(commit.stats.files.keys())[:2],
            })

        result = _try_ai_blame(blame_data)
        if not result:
            import random
            console.print(f"  [bold yellow]🔍 GIT BLAME BUT MAKE IT PERSONAL:[/bold yellow]\n")
            for item in blame_data:
                comment = random.choice(BLAME_FALLBACK)
                console.print(f"  [white]commit:[/white] [dim]{item['message']}[/dim]")
                console.print(f"  [yellow]→ {comment}[/yellow]\n")
        else:
            console.print(f"  [bold yellow]🔍 GIT BLAME BUT MAKE IT PERSONAL:[/bold yellow]\n")
            console.print(f"  [yellow]{result}[/yellow]\n")

    except Exception as e:
        console.print(f"  [red]error: {e}[/red]\n")

def _try_ai_blame(blame_data: list) -> str | None:
    try:
        from openai import OpenAI
        import os

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return None

        client = OpenAI(api_key=api_key)

        system = """You are a savage code historian.
You analyze git commits and roast each one personally.
For each commit, make a personal comment about the author's life choices.
Be funny, gen z, sarcastic. One line per commit max.
Respond in the same language the commits are written in."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=400,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": f"Blame these commits:\n{str(blame_data)}"}
            ]
        )
        return response.choices[0].message.content

    except Exception:
        return None