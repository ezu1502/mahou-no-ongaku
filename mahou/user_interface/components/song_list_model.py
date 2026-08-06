from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from mahou.core.song import Song
from typing import Literal
from contextlib import contextmanager

Roles = Qt.ItemDataRole

class SongListModel(QAbstractListModel):
    def __init__(self, database) -> None:
        super().__init__()

        self.database = database
        self.song_map: dict[int, Song] = self.database.song_map
        self.song_list: list[Song] = list(self.song_map.values())

    def rowCount(self, parent):
        return len(self.song_list)

    def data(self, index, role = Roles.DisplayRole):
        song = self.song_list[index.row()]

        if role == Roles.DisplayRole:
            return song.title
        elif role == Roles.UserRole:
            return song.id

        return None

    def get_song_from_index(self, index: int) -> Song:
        return self.song_list[index]

    def update_list_order(self, key: Literal["title", "id", "play_count"]):
        self.song_list.sort(key = lambda song: getattr(song, key))

    @contextmanager
    def reset_model(self):
        self.beginResetModel()

        try:
            yield
        finally:
            self.endResetModel()


            #! CONTINUAR DAQUI !!!!!!!!!!!!!1


            
    def set_songs(self, song):
        self.beginResetModel()

        self.song_list = list(self.song_map.values()) # ! terminar ainda, isso é um placeholder

        self.endResetModel()

