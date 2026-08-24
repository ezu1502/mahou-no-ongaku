from __future__ import annotations
from PySide6.QtCore import QAbstractListModel, QByteArray, Qt, QSortFilterProxyModel, QModelIndex
from mahou.song import Song
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.database.song_database import SongDatabase

Roles = Qt.ItemDataRole

class SongModel(QAbstractListModel):
    ARTIST_ROLE = Roles.UserRole + 1
    PATH_ROLE = Roles.UserRole + 2

    def __init__(self, database: SongDatabase):
        super().__init__()

        self.database = database

        self.song_list: list[Song] = self.database.get_song_list()


    def roleNames(self):
        return {
            Roles.DisplayRole: b"title",
            self.ARTIST_ROLE: b"artist",
            self.PATH_ROLE: b"path",
        }
        
    def rowCount(self, parent = None) -> int:
        return len(self.song_list)


    def data(self, index: QModelIndex, role: int = Roles.DisplayRole):
        if not index.isValid():
            return None

        song = self.song_list[index.row()]

        if role == Roles.DisplayRole:
            return song.title

        if role == self.ARTIST_ROLE:
            # return song.metadata.artist if song.has_metadata() else "Unknown"
            #TODO implementar
            return "Unknown"

        if role == self.PATH_ROLE:
            return str(song.path)

        return None

    
class SongProxy(QSortFilterProxyModel):
    def __init__(self, model: SongModel):
        super().__init__()

        self.setSourceModel(model)



    