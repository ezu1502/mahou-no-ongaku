from __future__ import annotations
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QObject, QUrl, Signal

from pathlib import Path

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ongaku.core.app import App

class Player(QObject):
    positionChanged = Signal(int)
    durationChanged = Signal(int)

    # todo CONTINUAR AQUI! Linkar sinal ao Qml pra controlar a progressbar

    def __init__(self, app: App):
        super().__init__()

        self.app: App = app

        self.media = QMediaPlayer()
        self.output = QAudioOutput()

        self.media.setAudioOutput(self.output)

        self.media.durationChanged.connect(self.durationChanged)
        self.media.positionChanged.connect(self.positionChanged)


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