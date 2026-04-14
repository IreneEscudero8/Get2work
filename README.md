# get2work 

> The Python library that makes you actually work.

[![PyPI version](https://badge.fury.io/py/get2work.svg)](https://badge.fury.io/py/get2work)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

get2work is a CLI tool that gamifies your coding productivity. It celebrates your commits, roasts your git history, shames you when you're slacking, and makes you actually ship things.

## Features

-  **Commit celebrations** — animations and sounds every time you commit
-  **Level system** — 8 levels from "Hello World Survivor" to "Linus Would Be Proud"
-  **Streak tracking** — daily commit streaks
-  **Shame notifications** — get roasted if you haven't committed today
-  **AI roasts** — your commit history analyzed and destroyed by AI
-  **Vibe check** — AI mental health diagnosis based on your commits
-  **Peer pressure** — see what other devs are shipping and feel bad
-  **Pomodoro timer** — focus sessions that count toward your level
-  **Accountability receipt** — daily summary of what you actually did
-  **Code funeral** — deleting 100+ lines triggers a funeral 
-  **Git blame but personal** — AI roasts each commit individually

##  Installation

```bash
pip install get2work
```

##  Quick Start

```bash
# Install the git hook in your repo (do this once per project)
get2work install

# Check your level and stats
get2work status

# Now just commit normally and watch the magic happen
git commit -m "feat: add something cool"
```

##  Commands

| Command | Description |
|---|---|
| `get2work install` | Install git hook in current repo |
| `get2work status` | Your level, streak, and stats |
| `get2work roast` | Get your commits roasted by AI  |
| `get2work vibe` | AI mental health diagnosis  |
| `get2work blame` | Git blame but make it personal  |
| `get2work peer <username>` | Stalk a dev on GitHub  |
| `get2work randompeer` | Random dev from the internet  |
| `get2work pomodoro` | Start a pomodoro timer  |
| `get2work shame` | Check if you deserve to be shamed  |
| `get2work receipt` | Your accountability receipt  |
| `get2work start` | Start background watcher |

##  AI Features (Optional)

The `roast`, `vibe`, and `blame` commands use AI for better results. Without an API key they fall back to hardcoded funny responses.

To enable AI roasts set your OpenAI API key:

```bash
export OPENAI_API_KEY="sk-..."
```

## Custom Sounds

Replace default sounds with your own by setting environment variables:

```bash
export GET2WORK_SOUND_CELEBRATE="/path/to/your/sound.mp3"
export GET2WORK_SOUND_FUNERAL="/path/to/funeral.mp3"
export GET2WORK_SOUND_SHAME="/path/to/shame.mp3"
export GET2WORK_SOUND_LEVELUP="/path/to/levelup.mp3"
```

## Level System

| Level | Name | Commits needed |
|---|---|---|
| 1 | Hello World Survivor | 0 |
| 2 | Tutorial Finisher | 10 |
| 3 | Functional but Confused | 30 |
| 4 | It Works Don't Touch It | 60 |
| 5 | Commits with Confidence (wrongly) | 100 |
| 6 | git push --force and it worked | 200 |
| 7 | The Last Line of Defense | 400 |
| 8 | Linus Would Be Proud | 700 |

## Tutorial

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](COLAB_LINK_HERE)

## Docker

```bash
docker build -t get2work .
docker run get2work
```
