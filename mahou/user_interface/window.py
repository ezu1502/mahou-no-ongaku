from PySide6.QtWidgets import (QMainWindow, QSizePolicy)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QCloseEvent
from mahou_libs.time_functions import TimeCounter
from pathlib import Path
from mahou.core.enums import Themes, Settings
from mahou.user_interface.main_screen import MahouMainScreen
from mahou import file_manager
from mahou.user_interface.components.menu_bar import MahouMenuBar

align = Qt.AlignmentFlag
size_policy = QSizePolicy.Policy

WINDOW_TITLE = "MAHOU NO ONGAKU - True Music Player"
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600

class MahouInterface(QMainWindow):
    theme_changed = Signal(Themes)

    @TimeCounter
    def __init__(self, app):
        super().__init__()
        
        self.app = app
        self.player = app.player

    
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.current_theme = self.get_theme_from_options()

        self.set_theme(
            self.current_theme if self.current_theme is not None else Themes.DARK,
            first_time = True
        )

        self.main_screen = MahouMainScreen(main_window = self, app = self.app)
        
        self.setCentralWidget(self.main_screen)

        self.menu_bar = MahouMenuBar(self.current_theme)
        self.setMenuBar(self.menu_bar)
        self.connect_menu_bar()

        self.theme_changed.connect(self.on_theme_changed)
    
# region THEME
    def load_stylesheet_string(self, style_path: Path | str):
        if isinstance(style_path, str):
            style_path = Path(style_path)

        return style_path.read_text(encoding = "utf-8")

    def get_theme_from_options(self) -> Themes | None:
        theme = file_manager.get_setting("theme")
        match theme:
            case "main_theme":
                return Themes.DARK
            case "light_theme":
                return Themes.LIGHT
            case "habanero_theme":
                return Themes.HABANERO
            case _:
                return None

    def on_theme_changed(self, theme: Themes):
        self.main_screen.update_highlight_theme(theme = theme)
        self.main_screen.show_now_playing(just_update_color = True)

    def apply_theme(self, theme):
        match theme:
            case Themes.DARK:
                style_path = Path(__file__).parent / "styles" / "dark_theme.qss"
            case Themes.LIGHT:
                style_path = Path(__file__).parent / "styles" / "light_theme.qss"
            case Themes.HABANERO:
                style_path = Path(__file__).parent / "styles" / "habanero_theme.qss"
            case _:
                style_path = Path(__file__).parent / "styles" / "dark_theme.qss"

        stylesheet_string = self.load_stylesheet_string(style_path)
        self.app.set_stylesheet(stylesheet_string)
  
    def set_theme(self, theme: Themes = Themes.DARK, first_time = False):
        if theme == self.current_theme and not first_time:
            return 

        self.apply_theme(theme)

        self.current_theme = theme
    
        if not first_time:
            file_manager.save_setting(theme.value, "theme")
            self.theme_changed.emit(theme)


#endregion
#region Menubar
    def connect_menu_bar(self):
        self.menu_bar.theme_chosen.connect(self.set_theme)
        self.menu_bar.open_folder_requested.connect(self.main_screen.scan_folder)
        self.menu_bar.toggle_folder_button_signal.connect(self.main_screen.toggle_folder_button_visibility)
        self.menu_bar.toggle_restart_button_signal.connect(self.main_screen.toggle_restart_button_visibility)

#endregion
        
    def set_window_title(self, song_title = None, reset = False):
            if reset:
                self.setWindowTitle(WINDOW_TITLE)
                return
            
            MAX_SIZE = 37
            if song_title is None:
                return
            
            if len(song_title) > MAX_SIZE:
                song_title = song_title[:MAX_SIZE - 1] + "…"
    
            if song_title:
                self.setWindowTitle(f"{song_title} - MAHOU NO ONGAKU")


    def save_configs(self):
        current_item = self.main_screen.playing_item
        if current_item is None:
            return
        
        position = self.player.get_pos()
        song_id = current_item.data(Qt.ItemDataRole.UserRole)
        configs_dict = {
            Settings.CURRENT_SONG_ID : song_id,
            Settings.SONG_POS : position,
        }

        file_manager.save_setting(configs_dict, "playing_configs")


    def closeEvent(self, event: QCloseEvent):
        self.main_screen.bridge.stop_song()
        
        self.save_configs()
        print("Playing configs saved.\nClosing window...")
        event.accept()