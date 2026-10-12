from __future__ import annotations
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QObject, QUrl

from pathlib import Path

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ongaku.app import App

class Player(QObject):
    def __init__(self, app: App):
        super().__init__()

        self.app: App = app

        self.media = QMediaPlayer()
        self.output = QAudioOutput()

        self.media.setAudioOutput(self.output)


    def load_path(self, song_path: Path) -> None:
        self.media.setSource(QUrl.fromLocalFile(str(song_path)))

    def play(self) -> None:
        self.media.play()

    def load_and_play(self, song_path: Path) -> None:
        self.load_path(song_path)
        self.play()

    def pause(self) -> None:
        self.media.pause()

    def unpause(self) -> None:
        self.media.play()

    def stop(self, unload: bool = False) -> None:
        self.media.stop()

        if unload:
            self.media.setSource(QUrl())