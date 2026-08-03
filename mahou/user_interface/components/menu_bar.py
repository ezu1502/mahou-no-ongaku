from PySide6.QtWidgets import QMenuBar
from mahou.core.enums import Settings, Paths, Themes
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtCore import Signal

from mahou import file_manager

class MahouMenuBar(QMenuBar):
    theme_chosen = Signal(Themes)
    open_folder_requested = Signal()
    toggle_folder_button_signal = Signal(bool)
    toggle_restart_button_signal = Signal(bool)

    
    def __init__(self, current_theme):
        super().__init__()

        self.current_theme = current_theme

        self.setup_menu_bar()

    def setup_menu_bar(self):
        self.make_menubar_menus()

        self.set_file_menu()

        self.set_view_menu()

        self.set_themes_menu()

        self.set_shortcuts_menu()
        
    def make_menubar_menus(self):
        self.file_menu = self.addMenu("File")
        self.view_menu = self.addMenu("View")
        self.themes_menu = self.addMenu("Theme")
        self.shortcuts_menu = self.addMenu("Shortcuts")
        self.about_menu = self.addMenu("About")

    def set_file_menu(self):
        self.choose_folder_action = QAction("Choose Folder")
        self.choose_folder_action.setShortcut("Ctrl+O")
        self.choose_folder_action.triggered.connect(lambda: self.open_folder_requested.emit())

        self.file_menu.addAction(self.choose_folder_action)
        
    def set_view_menu(self):
        options_dict = file_manager.read_file(Paths.SETTINGS_FILE)
        view_options = options_dict.get(Settings.VIEW, {})

        self.view_restart_button = QAction("Restart Button")
        self.view_folder_button = QAction("Folder Button")

        self.view_restart_button.setCheckable(True)
        self.view_folder_button.setCheckable(True)

        self.view_restart_button.setChecked(view_options.get(Settings.RESTART_BUTTON, True))
        self.view_folder_button.setChecked(view_options.get(Settings.FOLDER_BUTTON, True))

        self.view_restart_button.toggled.connect(self.toggle_restart_button_signal)
        self.view_folder_button.toggled.connect(self.toggle_folder_button_signal)

        
        self.view_menu.addAction(self.view_restart_button)
        self.view_menu.addAction(self.view_folder_button)

    def set_themes_menu(self):
        self.themes_group = QActionGroup(self)

        self.dark_theme_action = QAction("Dark Theme")
        self.light_theme_action = QAction("Light Theme")
        self.habanero_theme_action = QAction("Habanero Theme")


        self.dark_theme_action.setCheckable(True)
        self.light_theme_action.setCheckable(True)
        self.habanero_theme_action.setCheckable(True)

        self.themes_group.addAction(self.dark_theme_action)
        self.themes_group.addAction(self.light_theme_action)
        self.themes_group.addAction(self.habanero_theme_action)

        self.themes_group.setExclusive(True) #Só dá pra escolher 1 por vez


        match self.current_theme:
            case Themes.DARK:
                self.dark_theme_action.setChecked(True)
            case Themes.LIGHT:
                self.light_theme_action.setChecked(True)
            case Themes.HABANERO:
                self.habanero_theme_action.setChecked(True)

        self.themes_group.triggered.connect(self.on_theme_group_triggered)
        self.themes_menu.addActions(self.themes_group.actions())

    def set_shortcuts_menu(self):
        self.stop_song_shortcut = QAction("Stop Song - [S]")
        self.shortcuts_menu.addAction(self.stop_song_shortcut)

    def on_theme_group_triggered(self, action):
            if action == self.dark_theme_action:
                theme = Themes.DARK
            elif action == self.light_theme_action:
                theme = Themes.LIGHT
            elif action == self.habanero_theme_action:
                theme = Themes.HABANERO

            self.theme_chosen.emit(theme)