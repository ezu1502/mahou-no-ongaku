import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator
from ongaku.database.commands import SQLCommands as Commands
from ongaku.song import Song

class Database:
    def __init__(self, app):
        self.app = app
        self.db_path: Path = Path(__file__).parent.parent.parent / "mahou.db"

    def initialize(self) -> None:
        schema = self.read_command(Commands.SCHEMA)

        with self.connection() as con:
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

    def get_song_id(self, song_path:Path):
        """
            Receives a song path and returns the matching song's id
        """

        ...


    def insert_song(self, song_path: Path, metadata: dict) -> bool:
        """
            Tries to insert a song into the database. Returns True if succesful, False if sqlite3 fails.
        """
        artist, album = metadata.get("artist"), metadata.get("album")
        
        allowed_keys = {"title", "date", "track_number"}
        values = {
            "path": str(song_path),

            **{key: value for key, value in metadata.items() if value and key in allowed_keys}
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


                # TODO CONTINUAR AQUI!
                # TODO IMPLEMENTAR LÓGICA DE INSERIR ARTISTA E ÁLBUM PARA CADA MÚSICA



                return True
        except sqlite3.IntegrityError:
            return False

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
                songs.append(Song(
                    path = Path(path),
                    custom_title = title,
                    play_count = play_count,
                    listen_time = listen_time
                ))

            return songs

