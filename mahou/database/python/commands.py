from enum import Enum
from pathlib import Path

general_commands_folder = Path(__file__).parent.parent / "sql" / "general_commands"
song_commands_folder = Path(__file__).parent.parent / "sql" / "song_commands"

class Commands:
    class General(Enum):
        CREATE_TABLE = general_commands_folder / "create_table.sql"

    class Song(Enum):
        CHECK_PATH_EXISTS = song_commands_folder / "check_path_exists.sql"
        INSERT_SONG = song_commands_folder / "insert_song.sql"