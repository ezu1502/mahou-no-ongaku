from __future__ import annotations
from typing import TYPE_CHECKING, Dict
lazy from PySide6.QtCore import QAbstractListModel, QByteArray, QSortFilterProxyModel, QModelIndex, Qt
from ongaku.song import Song

if TYPE_CHECKING:
    from ongaku.app import App

Roles = Qt.ItemDataRole

class ListModel(QAbstractListModel):
    def __init__(self, app: App, parent = None):
        super().__init__(parent)

        self.app: App = app
        self.database = self.app.database
        self.songs: list[Song] = self.database.get_all_songs()


    def rowCount(self, parent = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        
        return len(self.songs)

    def roleNames(self) -> Dict[int, QByteArray]:
        return {
            Roles.DisplayRole: QByteArray(b"title"),
            Roles.UserRole + 1: QByteArray(b"path"),
            Roles.UserRole + 2: QByteArray(b"play_count"),
            Roles.UserRole + 3: QByteArray(b"listen_time")
        }

    def data(self, index: QModelIndex, role: int = Roles.DisplayRole):

        if not (index.isValid() and 0 <= index.row() < len(self.songs)): 
            return None

        song = self.songs[index.row()]

        roles = {
            Roles.DisplayRole: song.title,
            Roles.UserRole + 1: str(song.path),
            Roles.UserRole + 2: song.play_count,
            Roles.UserRole + 3: song.listen_time
        }

        return roles.get(role)

    def reload(self) -> None:
        self.beginResetModel()
        self.songs = self.database.get_all_songs()
        self.endResetModel()

class ListProxy(QSortFilterProxyModel):
    def __init__(self, model: ListModel):
        super().__init__()
        self.model: ListModel = model

        self.setSourceModel(self.model)
