from enum import Enum, StrEnum
from pathlib import Path

class PS(Enum):
    PLAYING = "playing"
    PAUSED = "paused"
    STOPPED = "stopped"
    WELCOME_SCREEN = "welcome_screen"
    IN_MENU = "in_menu"
    SHUT_DOWN = "shut_down"

class Themes(Enum):
    DARK = "main_theme"
    LIGHT = "light_theme"
    HABANERO = "habanero_theme"


class Paths(Enum):
    SETTINGS_FILE = Path("mahou_files") / ("user_settings.json")


class Settings(StrEnum):
    DEFAULT_FOLDER = "default_folder"
    
    VIEW = "view"

    RESTART_BUTTON = "restart_button"
    FOLDER_BUTTON = "folder_button"
