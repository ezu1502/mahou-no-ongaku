from PySide6.QtWidgets import (QMainWindow, QSizePolicy, QWidget, QSlider)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from mahou_libs.time_functions import log_delta_time
from pathlib import Path
from mahou.core.enums import Themes
from mahou.user_interface.player_bridge import PlayerBridge


from mahou.user_interface.main_screen import MahouMainScreen

align = Qt.AlignmentFlag
size_policy = QSizePolicy.Policy

class MahouInterface(QMainWindow):
    @log_delta_time
    def __init__(self, app):
        super().__init__()
        
        self.app = app
        self.player = app.player

        self.user_options_dict = None

        self.WINDOW_TITLE = "MAHOU NO ONGAKU - True Music Player"
        WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.set_theme(Themes.MAIN)

        self.main_screen = MahouMainScreen(main_window = self, app = self.app)
        self.setCentralWidget(self.main_screen)

        self.setup_menu_bar()
    

    def load_stylesheet_string(self, style_path: Path | str):
        if isinstance(style_path, str):
            style_path = Path(style_path)

        return style_path.read_text(encoding = "utf-8")

    def set_theme(self, theme: Themes = Themes.MAIN):
        match theme:
            case Themes.MAIN:
                style_path = Path(__file__).parent / "styles" / "main_theme.qss"
            case Themes.LIGHT:
                style_path = Path(__file__).parent / "styles" / "light_theme.qss"
            case Themes.HABANERO:
                style_path = Path(__file__).parent / "styles" / "habanero_theme.qss"
            case _:
                style_path = Path(__file__).parent / "styles" / "main_theme.qss"

        stylesheet_string = self.load_stylesheet_string(style_path)
        self.setStyleSheet(stylesheet_string)
                    
    def setup_menu_bar(self):
        self.menu_bar = self.menuBar()

        self.file_menu = self.menu_bar.addMenu("File")
        self.view_menu = self.menu_bar.addMenu("View")
        self.themes_menu = self.menu_bar.addMenu("Theme")
        self.shortcuts_menu = self.menu_bar.addMenu("Shortcuts")
        self.about_menu = self.menu_bar.addMenu("About")

        self.choose_folder_action = QAction("Choose Folder")
        self.choose_folder_action.setShortcut("Ctrl+O")
        self.choose_folder_action.triggered.connect(self.main_screen.choose_folder)

        self.view_restart_button = QAction("Restart Button")
        self.view_restart_button.setCheckable(True)
        self.view_restart_button.toggled.connect(self.main_screen.toggle_restart_button_visibility)

        self.view_folder_button = QAction("Folder Button")
        self.view_folder_button.setCheckable(True)
        self.view_folder_button.toggled.connect(self.main_screen.toggle_folder_button_visibility)


        if self.user_options_dict is not None:
            self.view_restart_button.setChecked(self.user_options_dict["restart"])
            self.view_folder_button.setChecked(self.user_options_dict["folder"])
        else:
            self.view_restart_button.setChecked(True)
            self.view_folder_button.setChecked(True)


        self.dark_theme_action = QAction("Dark Theme")
        self.light_theme_action = QAction("Light Theme")
        
        self.stop_song_shortcut = QAction("Stop Song - [S]")

        self.shortcuts_menu.addAction(self.stop_song_shortcut)

        self.themes_menu.addAction(self.dark_theme_action)
        self.themes_menu.addAction(self.light_theme_action)

        self.view_menu.addAction(self.view_restart_button)
        self.view_menu.addAction(self.view_folder_button)

        self.file_menu.addAction(self.choose_folder_action)
    