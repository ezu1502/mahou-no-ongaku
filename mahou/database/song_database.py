from __future__ import annotations
from mahou.database.commands import Commands
from mahou.database.connection import get_connection
from pathlib import Path
import sqlite3
from typing_extensions import TYPE_CHECKING
from mahou.song import Song

if TYPE_CHECKING:
    from mahou.app import App

class SongDatabase:
    def __init__(self, app: App):
        self.app = app

        self.connection = get_connection()

        self.cursor = self.connection.cursor()

        print("Database initialized!")

    def commit(self):
        self.connection.commit()

    def initialize(self):
        self.cursor.execute(self.read_command(Commands.CREATE_TABLE))
        self.commit()

    def read_command(self, command: Commands) -> str:
        """ Recebe o Enum do comando e retorna o texto dele pro cursor executar
        """
        cmd_to_read = command.value
        cmd_text = None


        if cmd_to_read.exists():
            cmd_text = cmd_to_read.read_text()

        if not cmd_text or not cmd_text.strip():
            raise RuntimeError(f"Could not load command: '{command}'")

        return cmd_text

    def insert_song_path(self, song_path: Path, commit: bool = True) -> None:
        """ Insere uma música no database. Se ela já estiver lá, ótimo
        """

        try:
            self.cursor.execute(self.read_command(Commands.INSERT_SONG), (str(song_path), song_path.stem))
        except sqlite3.IntegrityError as error:
            print(f"\n{error} while inserting song path: {song_path}")
        else:
            if commit:
                self.commit()

    def get_song_list(self) -> list[Song]:
        """ Puxa todas as musicas do database, cria objetos Song na memória e retorna uma lista com eles
        """

        self.cursor.execute(self.read_command(Commands.GET_ALL_SONGS))

        songs = self.cursor.fetchall()

        song_list: list[Song] = []

        for song_id, path, title in songs:
            song = Song(id = song_id, path = Path(path), custom_title = title)
            song_list.append(song)

        return song_list
        



        

    
    
        