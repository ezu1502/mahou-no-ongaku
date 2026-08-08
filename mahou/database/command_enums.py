from enum import Enum, StrEnum
from pathlib import Path

class GeneralCommands(StrEnum):
    CREATE_TABLE = "general/create_table.sql"

class SongCommands(StrEnum):
    SEARCH_ID = "song/search_song_id.sql"
    SEARCH_PATH = "song/search_song_path.sql"

    CHECK_EXISTS = "song/check_song_exists.sql"
    INSERT_SONG = "song/insert_song.sql"
    INSERT_METADATA = "song/insert_metadata.sql"
    SELECT_ALL = "song/select_all_songs.sql"

    INCREMENT_PLAY_COUNT = "song/increment_play_count.sql"
    UPDATE_LISTEN_TIME = "song/update_listen_time.sql"

