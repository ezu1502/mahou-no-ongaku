import sqlite3
from pathlib import Path
from mahou.core.enums import Paths

database_path = Paths.DATABASE.value



def get_connection():
    database_path.parent.mkdir(parents = True, exist_ok= True)
    return sqlite3.connect(database_path)