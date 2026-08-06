from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from mahou.core.song import Song

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