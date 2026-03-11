import sqlite3
from pathlib import Path

DB_PATH = Path("storage/cache.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_cache():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS summaries (
            hash TEXT PRIMARY KEY,
            summary TEXT NOT NULL,
            model TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def get_cached_summary(text_hash: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT summary FROM summaries WHERE hash = ?",
        (text_hash,)
    )

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None


def store_summary(text_hash: str, summary: str, model: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO summaries (hash, summary, model)
        VALUES (?, ?, ?)
        """,
        (text_hash, summary, model)
    )

    conn.commit()
    conn.close()