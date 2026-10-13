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

    def __init__(self, app: App):
        super().__init__()

        self.app: App = app

        self.media = QMediaPlayer(self)
        self.output = QAudioOutput(self)

        self.media.setAudioOutput(self.output)

        self.media.durationChanged.connect(self._on_duration_changed)
        self.media.positionChanged.connect(self._on_position_changed)

        self.loaded_path: Path | None = None

    def _on_duration_changed(self, duration: int) -> None:
        self.durationChanged.emit(duration)

    def _on_position_changed(self, position: int) -> None:
        self.positionChanged.emit(position)

    def set_position(self, position_ms: int) -> None:
        self.media.setPosition(position_ms)

    def load_path(self, song_path: Path) -> None:
        self.media.setSource(QUrl.fromLocalFile(str(song_path)))
        self.loaded_path = song_path

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

        self.durationChanged.emit(0)