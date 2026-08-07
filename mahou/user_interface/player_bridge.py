from __future__ import annotations

from mahou.core.enums import PS
from PySide6.QtGui import QColor, QBrush
from PySide6.QtCore import Qt
from mahou_libs.time_functions import TimeCounter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mahou.user_interface.main_screen import MahouMainScreen

#region PLAYER CONTROLS
class PlayerBridge:
    def __init__(self, master: MahouMainScreen):
        self.master = master

        self.player = self.master.player
        
        self.player.state_changed.connect(self.master.update_UI_by_state)
        self.player.song_ended.connect(lambda: self.change_song(1))

        self.set_window_title = self.master.main_window.set_window_title

        self.app = self.master.app

        self.no_need_to_load = False

    @TimeCounter
    def toggle(self):
        match self.get_state():
            case PS.PLAYING:
                self.player.pause_song()
            case PS.PAUSED:
                self.player.play_song()
            case PS.IN_MENU:
                self.load_and_play()

    def load_and_play(self, specific_item = None, play = True):
        if specific_item is None:
            song = self.master.selected_song
            if song is None:
                return
        else:
            song = specific_item
        
        self.player.load_song(song)

        if play:
            self.player.play_song()

        self.master.update_listbox_UI() # ! corrigir
    
        self.master.set_playing_song(song)
        self.master.see_item(song)

        song_title = song.title
        self.show_now_playing(song_title)
        self.set_window_title(song_title = song_title)



    def play_selected(self):
        self.load_and_play()
        # self.master.update_UI_by_state()

    def play_without_loading(self):
        self.player.play_song()

    def stop_song(self):
        self.master.set_playing_song(None)

        self.player.stop_song()
    
        self.master.hide_now_playing()
        self.master.reset_listbox_UI()
        self.master.manage_play_selected_button()
        self.app.set_state(PS.IN_MENU)
        
        self.master.update_UI_by_state()
        self.set_window_title(reset = True)
        

    def restart_song(self):
        self.player.set_pos(0)
        

    def change_song(self, change):
        if self.player.loaded_song is None or self.master.playing_song is None:
            return
        if change == 0:
            return
        if change not in (-1, 1):
            raise ValueError(f"Unexpected change value: ({change}). \nChange in function change_song must be between (-1) and (1)")

        model = self.master.list_model
        proxy = self.master.proxy

        item_count = proxy.rowCount() #número de rows

        if item_count == 0:
            return

        current_song = self.master.playing_song

        with TimeCounter("Model <-> Proxy song index dialog"):
            # * acha o QModelIndex correspondente à música 
            source_index = model.model_index_from_song(current_song)

            if source_index is None:
                return

            # * mapeia o index achado pro proxy
            proxy_index = proxy.mapFromSource(source_index)

            if not proxy_index.isValid():
                return

            
            row = proxy_index.row() # * Encontra a row correspondente ao index do proxy

            new_row = (row + change) % item_count # * Efetua a mudança de música

            new_proxy_index = proxy.index(new_row, 0) # * encontra o QModelIndex do proxy correspondente à row nova

            new_source_index = proxy.mapToSource(new_proxy_index) # * mapeia o index pro model, que vai procurar na song_list

            new_song = model.get_song_from_model_index(new_source_index) # * Finalmente, obtém um objeto Song tocável

        if new_song is None:
            return

        # * Decide o que fazer com a música encontrada
        match self.get_state():
            case PS.PLAYING | PS.IN_MENU:
                self.load_and_play(new_song)
            case PS.PAUSED:
                self.load_and_play(new_song)
                self.player.pause_song()
            
#endregion
#region UI Updating
    def get_state(self):
        return self.app.state
    
    def set_state(self, state: PS):
        self.app.set_state(state)

    def show_now_playing(self, text: str):
        self.master.show_now_playing(text)