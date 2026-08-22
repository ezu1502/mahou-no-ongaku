from mahou.database.python.connection import get_connection
from mahou.database.python.commands import Commands
from pathlib import Path
import sqlite3

class Database:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor()


    def initialize(self):
        self.cursor.execute(self.load_command(Commands.General.CREATE_TABLE))
        self.connection.commit()


    def load_command(self, command: Commands.General | Commands.Song):

        command_path = command.value

        if not command_path.exists():
            raise FileNotFoundError(f"Couldn't find file: {command_path}")

        return command_path.read_text()



    def song_exists(self, song_path: Path | str):
        command_text = self.load_command(Commands.Song.CHECK_PATH_EXISTS)
        self.cursor.execute(command_text, (str(song_path), ))

        return self.cursor.fetchone() is not None

    def insert_song_path(self, song_path: Path | str, *, commit = True):
        command_text = self.load_command(Commands.Song.INSERT_SONG)

        try:
            self.cursor.execute(command_text, (str(song_path), Path(song_path).stem))
        except sqlite3.IntegrityError:
            # print("Failed adding song")
            return

        if commit:
            self.connection.commit()
        




        
