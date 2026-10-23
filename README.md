# Music Finder Bot

A Telegram bot for finding songs by title, artist, lyrics, links, or audio recognition support.

## Features
- Search by song title or artist
- Search by lyric words
- Support for iTunes and MusicBrainz music metadata
- SQLite local database for users, history, favorites, and bot settings
- Admin-only panel
- Arabic-first user experience with English support
- Clear error handling and rate-safe requests

## Stack
- Python 3.12+
- aiogram 2.x
- aiohttp
- aiosqlite
- python-dotenv

## Setup
1. Create and activate a virtual environment.
2. Install requirements:
   pip install -r requirements.txt
3. Copy `.env.example` to `.env` and fill values.
4. Run:
   python main.py

## BotFather
1. Open Telegram and start @BotFather.
2. Run `/newbot`.
3. Choose a name and username.
4. Copy the token to `BOT_TOKEN` in `.env`.

## Environment variables
See `.env.example`.

## Admin panel
Set `ADMIN_ID` to your Telegram user ID.

## Notes
- iTunes and MusicBrainz are used as free metadata sources.
- YouTube Data API and audio recognition require an external API key and quota.
- No audio files are stored by default.

## Hosting
This project is ready for local use and compatible with Railway, Render, or a Linux VPS.
