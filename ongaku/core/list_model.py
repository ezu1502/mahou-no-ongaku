from __future__ import annotations
from typing import TYPE_CHECKING, Dict
lazy from PySide6.QtCore import QAbstractListModel, QByteArray, QSortFilterProxyModel, QModelIndex, Qt
from ongaku.core.song import Song
from contextlib import contextmanager

if TYPE_CHECKING:
    from ongaku.core.app import App
    from ongaku.database.database import Database

Roles = Qt.ItemDataRole


class ListModel(QAbstractListModel):
    def __init__(self, app: App, parent = None):
        super().__init__(parent)

        self.app: App = app
        self.database: Database = self.app.database
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
            Roles.UserRole + 3: QByteArray(b"listen_time"),
            Roles.UserRole + 4: QByteArray(b"artists")
        }

    def data(self, index: QModelIndex, role: int = Roles.DisplayRole):

        if not (index.isValid() and 0 <= index.row() < len(self.songs)): 
            return None

        song = self.songs[index.row()]

        roles = {
            Roles.DisplayRole: song.title,
            Roles.UserRole + 1: str(song.path),
            Roles.UserRole + 2: song.play_count,
            Roles.UserRole + 3: song.listen_time,
            Roles.UserRole + 4: ", ".join(song.artists)
        }

        return roles.get(role)


    def reload(self) -> None:
        with self.reset_model():
            self.songs = self.database.get_all_songs()

    @contextmanager
    def reset_model(self):
        self.beginResetModel()
        try:
            yield
        finally:
            self.endResetModel()

class ListProxy(QSortFilterProxyModel):
    def __init__(self, model: ListModel):
        super().__init__()
        self.list_model: ListModel = model

        self.setSourceModel(self.list_model)
