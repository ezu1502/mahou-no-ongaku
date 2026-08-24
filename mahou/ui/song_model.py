
from PySide6.QtCore import QAbstractListModel, Qt

class SongModel(QAbstractListModel):
    def __init__(self, app):
        super().__init__()

        self.app = app


    