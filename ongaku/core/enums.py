from enum import Enum, auto

class PlayerState(Enum):
    PLAYING = auto()
    PAUSED = auto()
    MENU = auto()
