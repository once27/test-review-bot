import sqlite3

def get_connection():
    conn = sqlite3.connect("data.db")
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def safe_query(query, params=()):
    with get_connection() as conn:
        return conn.execute(query, params).fetchall()
