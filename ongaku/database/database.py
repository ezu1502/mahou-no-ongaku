import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator
from ongaku.database.commands import SQLCommands as Commands
from ongaku.core.song import Song

class Database:
    def __init__(self, app):
        self.app = app
        self.db_path: Path = Path(__file__).parent.parent.parent / "mahou.db"

    def initialize(self) -> None:
        schema = self.read_command(Commands.SCHEMA)

        with self.connection() as con:
            print(schema)
            con.executescript(
                "BEGIN;\n"
                + schema
                + "\nCOMMIT;"
            )

    @contextmanager
    def connection(self, commit: bool = True) -> Generator[sqlite3.Connection, None, None]:
        connection = sqlite3.connect(str(self.db_path))
        try:
            connection.execute("PRAGMA foreign_keys = ON")
            yield connection

            if commit:
                connection.commit()

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()

    def read_command(self, command: Commands) -> str:
        command_text = command.path.read_text(encoding = "utf-8")

        if not command_text.strip():
            raise ValueError(f"The command {str(command.path)} is empty")

        return command_text

    def get_song_id(self, song_path:Path, connection: sqlite3.Connection | None = None) -> int | None:
        """
            Receives a song path and returns the matching song's id
        """

        if connection is None:
            with self.connection(commit = False) as con:
                return self.get_song_id(song_path, connection = con)
        else:
            result = connection.execute(
                self.read_command(Commands.GET_SONG_ID),
                (str(song_path),)
            ).fetchone()

            return result[0] if result is not None else None


    def insert_song_artist(self, artist_name: str, song_path: Path, connection: sqlite3.Connection) -> bool:
        artist_id = connection.execute(
            self.read_command(Commands.GET_ARTIST_ID),
            (artist_name,)
        ).fetchone()

        if artist_id is None:
            artist_id = connection.execute(
                self.read_command(Commands.CREATE_ARTIST),
                (artist_name,)
            ).fetchone()

        song_id = connection.execute(
            self.read_command(Commands.GET_SONG_ID),
            (str(song_path),)
        ).fetchone()

        if song_id is None or artist_id is None:
            return False

        song_id, artist_id = song_id[0], artist_id[0]

        try:
            connection.execute(
                self.read_command(Commands.INSERT_SONG_ARTIST),
                (song_id, artist_id)
            )
        except sqlite3.IntegrityError:
            return False

        return True


    def insert_song(self, song_path: Path, metadata: dict) -> bool:
        """
            Tries to insert a song into the database. Returns True if succesful, False if sqlite3 fails.
        """
        artist, album = metadata.get("artist"), metadata.get("album")
        
        allowed_keys = {"title", "date", "track_number"}
        values = {
            "path": str(song_path),

            **{key: value for key, value in metadata.items() if value is not None and key in allowed_keys}
        }

        """
            This creates a dynamic SQL query, only inserting not NULL values without having to create multiple
            .sql files
        """

        columns = ", ".join(values)
        placeholders = ", ".join("?" for _ in values)

        query = (
            f"INSERT INTO songs ({columns})\n"
            f"VALUES ({placeholders})"
        )

        try:
            with self.connection() as con:
                con.execute(query, tuple(values.values()))

                if artist is not None:
                    result = self.insert_song_artist(artist, song_path, con)
                    if not result:
                        raise RuntimeError("Couldn't link artist to song")

                return True
        except sqlite3.IntegrityError:
            return False

    def get_song_artists(self, song_path: Path, *, connection: sqlite3.Connection | None = None) -> list[str]:
        """
            Receives a song path and returns a list of its artists
        """

        if connection is None:
            with self.connection(commit = False) as con:
                return self.get_song_artists(song_path, connection = con)

        artists = connection.execute(
            self.read_command(Commands.GET_SONG_ARTISTS),
            (str(song_path),)
        ).fetchall()

        return [row[0] for row in artists]

    def get_all_songs(self) -> list[Song]:
        """
            Returns a list containing Song objects, representing database's full song library
        """
        songs: list[Song] = []

        with self.connection(commit = False) as con:
            result = con.execute(
                self.read_command(Commands.SELECT_ALL_SONGS)
            ).fetchall()


            for path, title, play_count, listen_time in result:
                song_path = Path(path)

                songs.append(Song(
                    path = song_path,
                    custom_title = title,
                    play_count = play_count,
                    listen_time = listen_time,
                    artists = self.get_song_artists(path, connection = con)
                ))

            return songs

