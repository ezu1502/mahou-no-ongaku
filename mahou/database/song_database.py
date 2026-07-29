from .connection import get_connection
from pathlib import Path
from enum import StrEnum

class Commands(StrEnum):
    CREATE_TABLE = "create_table.sql"
    INSERT_SONG = "insert_song.sql"

class SongDatabase:
    def __init__(self) -> None:
        self.connection = get_connection()
        self.cursor = self.connection.cursor()

    def initialize(self):
        self.create_table()
        #vem mais coisa aqui depois

    def create_table(self):
        self.cursor.executescript(self.load_command(Commands.CREATE_TABLE))
        self.connection.commit()

    def insert_song(self, title: str, song_path: Path | str):
        """ Coloca uma música no banco de dados. Não esqueça de commitar depois de usar! """
        self.cursor.execute(self.load_command(Commands.INSERT_SONG), (title, str(song_path)))

    def commit(self):
        self.connection.commit()

    def load_command(self, command: Commands) -> str:
        """ Lê o comando escrito num arquivo .sql, retorna uma string """
        sql_path = Path(__file__).parent / "sql_commands" / command

        if not sql_path.exists():
            raise FileNotFoundError(f"Caminho de comando não encontrado! {sql_path}")
        
        return sql_path.read_text(encoding = "utf-8")
