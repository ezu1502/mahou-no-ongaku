from pathlib import Path
from PySide6.QtCore import QObject, QUrl, Signal
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from mahou.core.song import Song
from mahou.core.enums import PS
from mahou_libs.time_functions import TimeCounter
PlayerState = QMediaPlayer.PlaybackState
import time

class SongTimer:
    def __init__(self) -> None:
        self._accumulated = 0
        self.total_time = None

        self.last_start = None
        self.stopped = False

        self.play()

    def play(self):
        if self.stopped:
            raise RuntimeError("Timer instance already stopped cannot be called again")
        
        if self.last_start is None:
            self.last_start = time.monotonic()

    def pause(self):
        if self.last_start is None:
            return
        now = time.monotonic()
        delta = now - self.last_start

        self.last_start = None
        self._accumulated += delta

    def stop(self):
        self.pause()
        self.stopped = True

        return self._accumulated



class MahouPlayer(QObject):
    state_changed = Signal()
    song_ended = Signal()

    position_changed = Signal(int)
    duration_changed = Signal(int)

    song_was_listened = Signal()

    def __init__(self, app):
        super().__init__()

        self.app = app
        self.loaded_song = None

        self.media_player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)

        self.media_player.setAudioOutput(self.audio_output)

        self.connect_signals()

        self.playing_song = None
        self.timer = None

    def connect_signals(self):
        self.media_player.playbackStateChanged.connect(self.handle_playback_state) #Estado do playback mudou
        self.media_player.mediaStatusChanged.connect(self.handle_media_status) #Status da media mudou
        self.media_player.durationChanged.connect(self.handle_duration_changed) #Duração total mudou
        self.media_player.positionChanged.connect(self.handle_position_changed)
        

    def handle_duration_changed(self, duration: int):
        self.duration_changed.emit(duration)

    def handle_position_changed(self, position: int):
        self.position_changed.emit(position)

    def handle_media_status(self, status: QMediaPlayer.MediaStatus):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            print("Song ended!")
            self.song_ended.emit()

    def handle_playback_state(self, state: PlayerState):
        match state:
            case PlayerState.PlayingState:
                self.app.set_state(PS.PLAYING)
            case PlayerState.PausedState:
                self.app.set_state(PS.PAUSED)
            case PlayerState.StoppedState:
                # self.app.set_state(PS.IN_MENU)
                pass

        self.state_changed.emit()


    def load_song(self, song: Song):
        self.stop_timer()

        # ! CONTINUAR AQUI, FUNÇÃO DE ANOTAR TEMPO DE MÚSICA OUVIDO

        self.timer = None
        path = song.path.resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Song path {path} does not exist or is not a valid song path")

        self.loaded_song = song
        self.playing_song = song
        
        path_url = QUrl.fromLocalFile(str(path))

        self.media_player.setSource(path_url)

    def play_song(self):
        self.media_player.play()

        if self.timer is None:
            self.timer = SongTimer()
        else:
            self.timer.play()

    def pause_song(self):
        self.media_player.pause()
        if self.timer is not None:
            self.timer.pause()

    def stop_song(self):
        if self.timer is not None:
            total = self.timer.stop()
            self.timer = None

        self.media_player.stop()
        self.media_player.setSource(QUrl())

        

    def get_pos(self):
        """ Returns posision in milliseconds """
        return self.media_player.position()
    
    def set_pos(self, position):
        self.media_player.setPosition(position)


    def stop_timer(self):
        if self.timer is not None:
            total_time = self.timer.stop()

        if total_time >= 30:
            self.song_was_listened.emit()



