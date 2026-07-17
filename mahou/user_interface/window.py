from PySide6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget,
QListWidgetItem, QGridLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from mahou_libs.time_functions import log_delta_time
from pathlib import Path
from mahou.core.song import Song
from mahou.core.ENUMS import PS

align = Qt.AlignmentFlag

class MahouInterface(QMainWindow):
    def __init__(self, player, app):
        super().__init__()
        
        
        self.player = player
        self.app = app

        self.playing_item = None
        
        self.setWindowTitle("MAHOU NO ONGAKU - True Music Player")
        self.setFixedSize(900, 600)

        style_path = Path(__file__).parent / "styles" / "mahou_main_theme.qss"
        self.setStyleSheet(self.load_stylesheet_string(style_path))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
    
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(align.AlignTop)
        self.central_widget.setLayout(self.main_layout)

        self.set_interface_aspect()

        
    def set_interface_aspect(self):
        self.title = QLabel("Mahou no Ongaku")
        self.title.setObjectName("title")
        self.main_layout.addWidget(self.title, 2, alignment = align.AlignHCenter)

        self.middle_layout = QHBoxLayout()
        self.main_layout.addLayout(self.middle_layout, 14)

        self.listbox = QListWidget()
        self.listbox.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listbox.setAlternatingRowColors(True)

        self.middle_layout.addWidget(self.listbox, 9)
    
        self.right_panel_widget = QWidget()
        
        self.right_panel = QVBoxLayout()
        self.right_panel.setAlignment(align.AlignTop)

        self.right_panel_widget.setLayout(self.right_panel)

        self.middle_layout.addWidget(self.right_panel_widget, 8)

        self.play_pause_button = QPushButton("PLAY")
        self.play_pause_button.setFixedSize(300, 60)
        self.play_pause_button.pressed.connect(self.toggle)

        self.right_panel.addWidget(self.play_pause_button, alignment = align.AlignHCenter)

        self.folder_button = QPushButton("Choose Folder")
        self.folder_button.setFixedSize(300, 60)
        
        self.right_panel.addWidget(self.folder_button, alignment = align.AlignHCenter)

        self.set_listbox_list(self.song_list)


    @property
    def apps_music_list(self):
        return self.app.library.song_list

    def set_listbox_list(self, list_to_add: list[Song]):
        if list_to_add is None:
            return
        
        for item in list_to_add:
            song_item = QListWidgetItem(item.title)
            song_item.setData(Qt.ItemDataRole.UserRole, item)
            self.listbox.addItem(song_item)

    def load_stylesheet_string(self, style_path: Path | str):
        if isinstance(style_path, str):
            style_path = Path(style_path)

        return style_path.read_text(encoding = "utf-8")
    
    @property
    def song_list(self):
        return self.app.library.song_list
    
    @property
    def listbox_selection(self):
        item = self.listbox.currentItem()
        return item
    

    
    def toggle(self):
        match self.get_state():
            case PS.PLAYING:
                self.player.pause_song()
            case PS.PAUSED:
                self.player.unpause_song()
            case PS.IN_MENU:
                self.load_and_play()
        self.update_UI_by_state()

    def update_UI_by_state(self):

        match self.get_state():
            case PS.PAUSED | PS.IN_MENU:
                self.play_pause_button.setText("PLAY")
            case PS.PLAYING:
                self.play_pause_button.setText("PAUSE")


    def load_and_play(self):
        item = self.listbox_selection
        if item is None:
            return
        
        self.update_listbox_UI(new_item = item)

        self.playing_item = item

        song = item.data(Qt.ItemDataRole.UserRole)
  
        if song is None:
            return
    
        self.player.load_song(song)
        self.player.play_song()
        

    def update_listbox_UI(self, new_item):
        if self.playing_item is not None:
            self.playing_item.setForeground(QBrush())
            song_name = self.playing_item.data(Qt.ItemDataRole.UserRole).title
            self.playing_item.setText(song_name)

        text = new_item.text()
        new_item.setText(f"▶ {text}")
        new_item.setForeground(QColor("#FFFF00"))
        self.listbox.clearSelection()

    def get_state(self):
        return self.app.state
    
    def set_state(self, state: PS):
        self.app.state = state
        self.update_UI_by_state()

    
