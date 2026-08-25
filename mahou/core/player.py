from __future__ import annotations
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QObject, Signal
from mahou.core.enums import PlayerState as PS
from pathlib import Path

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.core.app import App
    
class MahouPlayer(QObject):

    playerStateChanged = Signal(PS)

    def __init__(self, app: App):
        super().__init__()

        self.app = app

        self.media = QMediaPlayer()
        self.audio_output = QAudioOutput()

        self.media.setAudioOutput(self.audio_output)

        self.loaded_path: None | Path = None
        self.playing_path: None | Path = None


    def load_song(self, song_path: Path) -> None:
        """ recebe o caminho, carrega no Qmediaplayer, checa se o Qurl for válido e atualiza o estado do player
        """

        path_url = QUrl.fromLocalFile(str(song_path))

        if not path_url.isValid():
            return
        
        self.media.setSource(path_url)

        self.loaded_path = song_path

    def play_song(self) -> None:
        if not self.media.source().isValid():
            print("Cannot play invalid QUrl")
            return

        self.media.play()

        self.playing_path = self.loaded_path

        self.playerStateChanged.emit(PS.PLAYING)

        # TODO Implementar play_count += 1 no database!
        # TODO depois também testar erros de load e play para não enviar estado enganoso para a UI

    def pause_song(self) -> None:
        self.media.pause()

        self.playerStateChanged.emit(PS.PAUSED)

    def stop_song(self) -> None:
        self.media.stop()

        self.playing_path = None

        self.playerStateChanged.emit(PS.MENU)
        
    def load_and_play(self, song_path: Path) -> None:
        self.load_song(song_path)
        self.play_song()






