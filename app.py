import streamlit as st
import json
import os
import shutil
import time
import hashlib
import re
import sqlite3
from datetime import date, datetime, timedelta
from typing import List, Dict, Any

# -------------------------
# Config & filenames
# -------------------------
DB_FILE = "library.db"
FINE_PER_DAY = 10
DEFAULT_LOAN_DAYS = 14
APP_TITLE = "📚 Library Management System"

# -------------------------
# Safe JSON helpers (Keep these for now, as some data will be stored as JSON strings in the DB)
# -------------------------
# ... (all your existing safe JSON helper functions)
def save_json(path: str, data: Any):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(path: str, default):
    if not os.path.exists(path):
        save_json(path, default)
        return default
    try:
        if os.path.getsize(path) == 0:
            save_json(path, default)
            return default
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # A bit redundant now, but keep for robustness if files are used
        return default
    except Exception:
        return default
# ... (all other helper functions like is_strong_password)


# -------------------------
# Database helpers
# -------------------------

def get_db_connection():
    """Establishes a connection to the SQLite database and sets row factory."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def init_db():
    """Initializes the database schema and populates with sample data."""
    conn = get_db_connection()
    c = conn.cursor()

    # Create books table
    c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            cover_url TEXT,
            description TEXT,
            genre TEXT,
            keywords TEXT,
            available INTEGER,
            added_on TEXT
        )
    """)

    # Create users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            mobile TEXT,
            email TEXT PRIMARY KEY,
            password_hash TEXT,
            role TEXT,
            favorites TEXT
        )
    """)

    # Create issued books table
    c.execute("""
        CREATE TABLE IF NOT EXISTS issued (
            user_email TEXT,
            book_id INTEGER,
            issue_date TEXT,
            due_date TEXT,
            returned INTEGER,
            return_date TEXT
        )
    """)

    # Populate with sample data only if tables are empty
    c.execute("SELECT COUNT(*) FROM books")
    if c.fetchone()[0] == 0:
        sample_books = [
            (1, "To Kill a Mockingbird", "Harper Lee", "https://m.media-amazon.com/images/I/81gepf1eMqL.jpg", "A classic novel exploring racial injustice and moral growth in the Deep South.", json.dumps(["Classic Fiction"]), json.dumps(["justice", "racism", "law"]), 1, str(date.today() - timedelta(days=40))),
            (2, "Clean Code", "Robert C. Martin", "https://images-na.ssl-images-amazon.com/images/I/41xShlnTZTL._SX374_BO1,204,203,200_.jpg", "A handbook of agile software craftsmanship.", json.dumps(["Software Engineering"]), json.dumps(["programming", "best practices", "code"]), 1, str(date.today() - timedelta(days=30))),
            (3, "Python Crash Course", "Eric Matthes", "https://images-na.ssl-images-amazon.com/images/I/51BpsT0LfJL._SX376_BO1,204,203,200_.jpg", "A hands-on introduction to programming with Python.", json.dumps(["Programming"]), json.dumps(["python", "beginner", "projects"]), 1, str(date.today() - timedelta(days=7))),
        ]
        c.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", sample_books)
    
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        sample_users = [
            ("Head Librarian", "9999999999", "librarian@example.com", hashlib.sha256("admin123".encode()).hexdigest(), "librarian", json.dumps([])),
            ("Demo User", "8888888888", "user@example.com", hashlib.sha256("user123".encode()).hexdigest(), "user", json.dumps([])),
        ]
        c.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", sample_users)
    
    conn.commit()
    conn.close()

# New data retrieval functions
def get_books_db() -> List[Dict[str, Any]]:
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return [{k: json.loads(v) if k in ['genre', 'keywords'] else v for k, v in b.items()} for b in books]

def get_users_db() -> List[Dict[str, Any]]:
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return [{k: json.loads(v) if k == 'favorites' else v for k, v in u.items()} for u in users]

def get_issued_db() -> List[Dict[str, Any]]:
    conn = get_db_connection()
    issued = conn.execute("SELECT * FROM issued").fetchall()
    conn.close()
    return [dict(rec) for rec in issued]
