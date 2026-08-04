from .connection import get_connection
from pathlib import Path
from enum import Enum
from mahou_libs.bocca import BoccaFiglia
from mahou_libs.time_functions import TimeCounter
from mahou.core.song import Song
from mahou.database.command_enums import SongCommands, GeneralCommands
import sqlite3
log = BoccaFiglia("song_database", "#9191FF")

# ! PADRÃO DO DATABASE: id, path, title, play_count, listen_time

class SongDatabase:
    def __init__(self) -> None:
        self.connection = get_connection()
        self.cursor = self.connection.cursor()

        self._song_map = None

    def initialize(self):
        self.create_table()
        #vem mais coisa aqui depois

    def create_table(self):
        self.cursor.executescript(self.load_command(GeneralCommands.CREATE_TABLE))
        self.connection.commit()

    def check_song_exists(self, song_path) -> bool:
        
        self.cursor.execute(self.load_command(SongCommands.CHECK_EXISTS), (str(song_path),))
        return self.cursor.fetchone() is not None

    def get_or_create_song(self, song_path: Path, custom_title: str | None = None, commit: bool = True) -> Song | None:
        """ Adiciona uma música ao database se ela não estiver lá. Retorna essa música também no formato Song """
        if custom_title is None:
            custom_title = song_path.stem

        if not self.check_song_exists(song_path):
            self.insert_song(song_path, custom_title)
            self.reset_song_map()
            if commit:
                self.commit()

        return self.search_song_by_path(song_path)

    def insert_song(self, song_path, song_title):
        self.cursor.execute(self.load_command(SongCommands.INSERT_SONG), (str(song_path), song_title))
    
    def commit(self):
        self.connection.commit()

    def load_command(self, command: GeneralCommands | SongCommands) -> str:
        """ Lê o comando escrito num arquivo .sql, retorna uma string """

        sql_path = Path(__file__).parent / "sql_commands" / command

        if not sql_path.exists():
            raise FileNotFoundError(f"Caminho de comando não encontrado! {sql_path}")
        
        return sql_path.read_text(encoding = "utf-8")

    def search_song_by_path(self, path: Path | str) -> Song | None:
        command = self.load_command(SongCommands.SEARCH_PATH)

        path = str(path)
        self.cursor.execute(command, (path,))

        result = self.cursor.fetchone()

        if result is None:
            return None

        return self._row_to_song(result)

    def from_database(self):
        ...

    @staticmethod
    def _row_to_song(row: sqlite3.Row) -> Song:
        return Song(
            id = row["id"],
            path = Path(row["path"]),
            title_ = row["title"],
            play_count = row["play_count"],
            listen_time = row["listen_time"],
        )
    
    @property
    def song_map(self) -> dict[int, Song]:
        """
        Retorna uma todas as músicas do banco de dados em ordem alfabética*

            Returns: 
                List[Song]: Lista de Songs
          
        """
        if self._song_map is not None:
            return self._song_map

        command = self.load_command(SongCommands.SELECT_ALL)
        self.cursor.execute(command)

        all_songs_list = self.cursor.fetchall()

        song_map: dict[int, Song] = {}

        for song_row in all_songs_list:
            song = self._row_to_song(song_row)
            song_map[song.id] = song

        self._song_map = song_map

        return self._song_map

    def reset_song_map(self):
        self._song_map = None

    def increment_song_play_count(self, song_id):
        """ Recebe um ID de uma música e incrementa o play_count dela"""

        self.cursor.execute(self.load_command(SongCommands.INCREMENT_PLAY_COUNT), (song_id,))

        self.commit()

    def update_song_listen_time(self, song_id, listen_time):
        """ Recebe um ID de uma música junto com o tempo da última sessão, depois atualiza no database
        o listen_time dela com esse valor
        """

        self.cursor.execute(self.load_command(SongCommands.UPDATE_LISTEN_TIME), (listen_time, song_id))
        self.commit()

