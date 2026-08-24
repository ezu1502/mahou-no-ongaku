from __future__ import annotations
from typing import Dict
from PySide6.QtCore import QAbstractListModel, QByteArray, Qt, QSortFilterProxyModel, QModelIndex
from mahou.song import Song
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.database.song_database import SongDatabase

Roles = Qt.ItemDataRole




class SongModel(QAbstractListModel):
    DISPLAY_ROLE = Roles.UserRole + 1
    ARTIST_ROLE = Roles.UserRole + 2
    PATH_ROLE = Roles.UserRole + 3

    def __init__(self, database: SongDatabase):
        super().__init__()

        self.database = database

        self.song_list: list[Song] = []

    def roleNames(self):
        return {
            self.DISPLAY_ROLE: b"id",
            self.ARTIST_ROLE: b"artist",
            self.PATH_ROLE: b"path",
        }
        
    def rowCount(self, parent = None):
        return len(self.song_list)


    def data(self, index: QModelIndex, role = DISPLAY_ROLE):
        if not index.isValid():
            return None

        song = self.song_list[index.row()]

        if role == self.DISPLAY_ROLE:
            return song.id

        if role == self.ARTIST_ROLE:
            # return song.metadata.artist if song.has_metadata() else "Unknown"
            #TODO implementar
            return "Unknown"

        if role == self.PATH_ROLE:
            return song.path

    
class SongProxy(QSortFilterProxyModel):
    def __init__(self, model: SongModel):
        super().__init__()

        self.setSourceModel(model)



    