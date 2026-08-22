import sqlite3
from pathlib import Path

def get_connection():
    database_file = Path(__file__).parent.parent.parent / "mahou_files" / "data" / "ongaku.db"

    connection = sqlite3.connect(database_file)

    return connection

