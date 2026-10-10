import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator
from ongaku.database.commands import SQLCommands as Commands

class Database:
    def __init__(self, app):
        self.app = app
        self.db_path: Path = Path(__file__).parent.parent.parent / "mahou.db"

    def initialize(self) -> None:
        with self.connection() as con:
            con.execute(
                self.read_command(Commands.SCHEMA)
            )

    @contextmanager
    def connection(self, commit: bool = True) -> Generator[sqlite3.Connection, None, None]:
        connection = sqlite3.connect(str(self.db_path))
        try:
            
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


    def insert_song(self, song_path: Path) -> bool:
        """
            Tries to insert a song into the database. Returns True if succesful, False if sqlite3 fails.
        """
        try:
            with self.connection() as con:
                con.execute(
                    self.read_command(Commands.INSERT_SONG),
                    (str(song_path),)
                )

                return True
        except sqlite3.IntegrityError:
            return False