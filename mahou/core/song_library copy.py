from pathlib import Path
from mahou.database.song_database import SongDatabase
from mahou.core.song import Song

class SongLibrary:
    def __init__(self, database: SongDatabase):
        self.database = database

    def get_songs(self):
        all_songs = self.database.get_all_songs()
        
        







