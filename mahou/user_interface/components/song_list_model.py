from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QColor, QBrush
from mahou.core.song import Song
from typing import Literal
from contextlib import contextmanager

from mahou_libs.time_functions import TimeCounter

Roles = Qt.ItemDataRole

class SongListModel(QAbstractListModel):
    def __init__(self, database) -> None:
        super().__init__()

        self.database = database

        self.song_map: dict[int, Song] = self.database.song_map
        self.song_list: list[Song] = list(self.song_map.values())

        self.playing_song: Song | None = None

    @TimeCounter
    def set_playing_song(self, song: Song | None):
        """ Troca a variável self.playing_song para um valor novo, e avisa que os valores mudaram para que a UI seja atualizada
        """
        if song is None:
            return

        old_song = self.playing_song
        self.playing_song = song

        if old_song is not None:
            old_model_index = self.model_index_from_song(old_song)
            if old_model_index is not None:
                self.dataChanged.emit(old_model_index, old_model_index, [Roles.ForegroundRole])

        new_model_index = self.model_index_from_song(self.playing_song)
        if new_model_index is not None:
            self.dataChanged.emit(new_model_index, new_model_index, [Roles.ForegroundRole])
 
            
        
        


        




    def model_index_from_song(self, song: Song) -> QModelIndex | None:
        try:
            row = self.song_list.index(song)
            return self.createIndex(row, 0)
        except ValueError:
            return None


    def model_index_from_row(self, row: int) -> QModelIndex:
        return self.createIndex(row, 0)
        
            

            



    def rowCount(self, parent = QModelIndex()) -> int:
        return len(self.song_list)

    def get_song(self, index: QModelIndex) -> Song | None:
        if not index.isValid():
            return None

        return self.song_list[index.row()]

    def int_index_from_song(self, song: Song) -> int:
        return self.song_list.index(song)
            
    
    

    


    def data(self, index, role = Roles.DisplayRole):
        if not index.isValid():
            return None

        
        song = self.song_list[index.row()]

        if role == Roles.DisplayRole:
            return song.title
        if role == Roles.UserRole:
            return song.id
        if role == Roles.ForegroundRole:
            if song == self.playing_song:
                return QBrush(QColor("#FFC400"))
            
            return None
       
        return None

    def update_list_order(self, key: Literal["title", "id", "play_count"]):
        with self.reset_model():
            self.song_list.sort(key = lambda song: getattr(song, key))






    @contextmanager
    def reset_model(self):
        self.beginResetModel()

        try:
            yield
        finally:
            self.endResetModel()



            
    def set_songs(self, song):
        with self.reset_model():
            self.song_list = list(self.song_map.values()) # ! terminar ainda, isso é um placeholder

    def _reload_song_list(self):
        with self.reset_model():
            self.song_list = list(self.song_map.values())
