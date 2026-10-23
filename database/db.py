import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "music_finder_bot.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            language TEXT DEFAULT 'ar',
            joined_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            query TEXT,
            search_type TEXT,
            results_count INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            track_id TEXT,
            track_title TEXT,
            artist_name TEXT,
            source_url TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS bot_settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def upsert_user(user_id, username, first_name, language='ar'):
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO users (user_id, username, first_name, language, joined_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            username = excluded.username,
            first_name = excluded.first_name,
            language = excluded.language
        """,
        (user_id, username, first_name, language, datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()


def add_search_history(user_id, query, search_type, results_count):
    conn = get_connection()
    conn.execute(
        "INSERT INTO search_history (user_id, query, search_type, results_count, created_at) VALUES (?, ?, ?, ?, ?)",
        (user_id, query, search_type, results_count, datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()


def get_search_history(user_id, limit=10):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM search_history WHERE user_id = ? ORDER BY id DESC LIMIT ?",
        (user_id, limit),
    ).fetchall()
    conn.close()
    return rows


def delete_search_history(user_id):
    conn = get_connection()
    conn.execute("DELETE FROM search_history WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


def add_favorite(user_id, track_id, track_title, artist_name, source_url):
    conn = get_connection()
    conn.execute(
        "INSERT INTO favorites (user_id, track_id, track_title, artist_name, source_url, created_at) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, track_id, track_title, artist_name, source_url, datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()


def get_favorites(user_id):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM favorites WHERE user_id = ? ORDER BY id DESC",
        (user_id,),
    ).fetchall()
    conn.close()
    return rows


def stats_users_count():
    conn = get_connection()
    count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    conn.close()
    return count


def stats_search_count():
    conn = get_connection()
    count = conn.execute("SELECT COUNT(*) FROM search_history").fetchone()[0]
    conn.close()
    return count
