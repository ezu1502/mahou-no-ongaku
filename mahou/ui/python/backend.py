from PySide6.QtCore import QObject, Property, Signal, Slot

class BackEnd(QObject):
    def __init__(self):
        super().__init__()