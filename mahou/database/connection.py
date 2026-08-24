import sqlite3
from pathlib import Path

def get_connection():
    database_path = Path(__file__).parent.parent.parent / "mahou_files" / "data" / "ongaku.db"

    database_path.parent.mkdir(parents = True, exist_ok = True)

    return sqlite3.connect(database_path)