from .connection import get_connection
from pathlib import Path
from enum import Enum
from mahou_libs.bocca import BoccaFiglia
from mahou_libs.time_functions import TimeCounter
from mahou.core.song import Song
from mahou.database.command_enums import SongCommands, GeneralCommands

log = BoccaFiglia("song_database", "#9191FF")

# ! PADRÃO DO DATABASE: (id, path, title)

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

    def insert_new_song(self, song_path: Path, custom_title = None, commit = True):
        if custom_title is None:
            custom_title = song_path.stem
        
        self.cursor.execute(self.load_command(SongCommands.INSERT_SONG), (str(song_path), custom_title))

        self.reset_song_map()
        
        if commit:
            self.commit()
       
    
    def commit(self):
        self.connection.commit()

    def load_command(self, command: GeneralCommands | SongCommands, subfolder = None) -> str:
        """ Lê o comando escrito num arquivo .sql, retorna uma string """

        if subfolder is not None:
            sql_path = Path(__file__).parent / "sql_commands" / subfolder / command
        else:
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

        return self._tuple_to_song(result)
        
    @staticmethod
    def _tuple_to_song(song_tuple: tuple[int, str, str]) -> Song:
        song_id, song_path, title = song_tuple

        return Song(id = song_id, path = Path(song_path), title_ = title)
    
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

        for song_info in all_songs_list:
            song = self._tuple_to_song(song_info)
            song_map[song.id] = song

        self._song_map = song_map

        return self._song_map

    def reset_song_map(self):
        self._song_map = None

