from enum import Enum
from pathlib import Path

cmd_path = Path(__file__).parent / "sql"

class Commands(Enum):
    CREATE_TABLE = cmd_path / "create_table.sql"

    INSERT_SONG = cmd_path / "insert_song.sql"
    CHECK_PATH_EXISTS = cmd_path / "check_path_exists.sql"

    GET_ALL_SONGS = cmd_path / "get_all_songs.sql"

    