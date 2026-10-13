from enum import Enum, auto
from pathlib import Path

COMMAND_FOLDER: Path = Path(__file__).parent / "sql"

class SQLCommands(Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
        return name.lower() + ".sql"

    SCHEMA = auto()

    INSERT_SONG = auto()
    SELECT_ALL_SONGS = auto()
    GET_SONG_ID = auto()

    INSERT_SONG_ARTIST = auto()
    GET_SONG_ARTISTS = auto()
    
    CHECK_ARTIST_EXISTS = auto()
    GET_ARTIST_ID = auto()
    CREATE_ARTIST = auto()

    @property
    def path(self) -> Path:
        return COMMAND_FOLDER / self.value

    