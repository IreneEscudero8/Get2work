# get2work 

> The Python library that makes you actually work.

[![PyPI version](https://img.shields.io/pypi/v/get2work.svg)](https://pypi.org/project/get2work/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

get2work is a CLI tool that gamifies your coding productivity. It celebrates your commits, roasts your git history, shames you when you're slacking, and makes you actually ship things.

## Features

-  **Commit celebrations** — ASCII animations and meme sounds every time you commit
-  **Level system** — 8 levels from "Hello World Survivor" to "Linus Would Be Proud", unlocked by commit count
-  **Streak tracking** — daily commit streaks, lose it if you skip a day
-  **Code funeral** — delete 100+ lines in a commit and get2work plays a funeral with sad trombone
-  **Shame notifications** — escalating messages if you haven't committed today. Starts gentle, ends personal
-  **AI roast** — your entire commit history analyzed and destroyed by AI. The "big picture" character assassination
-  **Git blame but personal** — AI roasts each individual commit. Line by line, no mercy
-  **Vibe check** — AI gives you a mental health diagnosis based on your commit patterns. Not medical advice. Probably accurate
-  **Peer pressure** — see what a specific dev OR a random dev from the internet is shipping, with sarcastic commentary
-  **Distraction detector** — detects if you have Netflix, Spotify, Discord, TikTok or other non-work apps open. Shames you in terminal AND sends a system notification pop-up you can't ignore
-  **Pomodoro timer** — focus sessions with countdown, each completed session counts toward your level
-  **Accountability receipt** — end of day summary formatted like a store receipt
-  **Custom sounds** — replace default meme sounds with your own audio files

## Installation

```bash
pip install get2work
```

## Quick Start

```bash
# 1. Install the git hook in your repo (once per project)
cd your-project
get2work install

# 2. Work normally — get2work handles the rest
git commit -m "feat: add something cool"
#  celebration appears automatically!
```

##  Commands

| Command | Description |
|---|---|
| `get2work install` | Install git hook in current repo — enables automatic celebrations |
| `get2work status` | Your level, streak, commits, pomodoros and distractions caught |
| `get2work roast` | AI roasts your entire commit history  |
| `get2work vibe` | AI mental health diagnosis based on your commits  |
| `get2work blame` | Git blame but make it personal — AI roasts each commit individually |
| `get2work peer <username>` | See what a specific GitHub user is shipping  |
| `get2work randompeer` | Get shamed by a completely random dev from the internet  |
| `get2work pomodoro` | Start a pomodoro timer (default 25min, use --minutes to change) |
| `get2work shame` | Check if you deserve to be shamed right now  |
| `get2work distraction` | Check if you have distracting apps open right now  |
| `get2work receipt` | Your accountability receipt for today  |
| `get2work start` | Start background watcher — monitors commits and distractions 24/7 |

##  Level System

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

##  AI Features (Optional)

`roast`, `vibe`, and `blame` use AI for unique responses every time. Without an API key they fall back to hardcoded funny responses — the library works fine without it.

```bash
export OPENAI_API_KEY="sk-..."
```

##  Distraction Detector

Detects distracting apps running on your system (Netflix, Spotify, Discord, TikTok, Steam, and more). When caught:
- Shames you in the terminal with a sarcastic message
- Sends a **system notification pop-up** so you can't ignore it (works on Mac, Linux, and Windows)
- Increments your `distractions_caught` counter visible in `get2work status`

Use `get2work start` to run it automatically every 2 minutes in the background.

##  Custom Sounds

Replace default meme sounds with your own:

```bash
export GET2WORK_SOUND_CELEBRATE="/path/to/airhorn.mp3"
export GET2WORK_SOUND_FUNERAL="/path/to/sad_trombone.mp3"
export GET2WORK_SOUND_SHAME="/path/to/bruh.mp3"
export GET2WORK_SOUND_LEVELUP="/path/to/levelup.mp3"
```

##  Tutorial

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10aUtSqItK1U6wZQ5E4ZSvVexkBftkwDH?usp=sharing)

##  Docker

```bash
docker build -t get2work .
docker run get2work
```
