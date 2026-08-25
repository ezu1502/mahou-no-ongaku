from __future__ import annotations
from enum import Enum, auto
from PySide6.QtCore import QAbstractListModel, QByteArray, Qt, QSortFilterProxyModel, QModelIndex
from mahou.core.song import Song
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.database.song_database import SongDatabase

Roles = Qt.ItemDataRole

class Filters(Enum):
    ALL = auto()
    PLAYLISTS = auto()
    ALBUMS = auto()
    ARTISTS = auto()


class SongModel(QAbstractListModel):
    SONG_ROLE = Roles.UserRole
    ARTIST_ROLE = Roles.UserRole + 1
    PATH_ROLE = Roles.UserRole + 2

    def __init__(self, database: SongDatabase):
        super().__init__()

        self.database = database

        self.song_list: list[Song] = self.database.get_song_list()

    def refresh_song_list(self) -> None:
        self.beginResetModel()
        self.song_list = self.database.get_song_list()
        self.endResetModel()

    def initialize(self):
        ...

    def roleNames(self):
        return {
            Roles.DisplayRole: b"title",
            self.ARTIST_ROLE: b"artist",
            self.PATH_ROLE: b"path",
            self.SONG_ROLE: b"song_obj",
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
            if song.metadata is not None and song.metadata.artist is not None:
                return song.metadata.artist

            return "Unknown"
        
        if role == self.PATH_ROLE:
            return str(song.path)

        if role == self.SONG_ROLE:
            return song

        return None

    
class SongProxy(QSortFilterProxyModel):
    def __init__(self, model: SongModel):
        super().__init__()

        self.setSourceModel(model)

        self.current_filter = Filters.ALL

        self.sort(0)

    def set_filter(self, filter: Filters):
        self.current_filter = filter
        self.invalidateFilter()

    def set_sorting_method(self, method):
        #TODO fazer essa implementação
        self.sort(0)


    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        match self.current_filter:
            case Filters.ALL:
                return True
            case Filters.PLAYLISTS:
                return False
            case Filters.ALBUMS:
                return False
            case Filters.ARTISTS:
                return False

        return False

    def lessThan(self, source_left: QModelIndex, source_right: QModelIndex) -> bool:
        left = source_left.data(Roles.DisplayRole)
        right = source_right.data(Roles.DisplayRole)

        return left.lower() < right.lower()



    