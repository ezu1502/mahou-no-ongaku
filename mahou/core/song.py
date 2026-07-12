from dataclasses import dataclass, field
from pathlib import Path
from bunseki import Analyzer
from mahou.core import cache_tools
#Cada música vai ser uma class agora

@dataclass
class Song:
    path: Path
    _analysis: None | Analyzer = field(
        default = None,
        init = False, # Não mostra o _analysis no construtor
        repr = False, # Não mostra o Analyzer quando referenciar (song)
        compare = False # Não diz que 2 musicas são diferentes só por uma ter sido analisada e outra não
    )   

    @property
    def analysis(self) -> Analyzer:
        if self._analysis is None:
            self._analysis = Analyzer(self.path)
        return self._analysis

#region BASICS
    @property
    def title(self) -> str:
        return self.path.stem
    
    @property
    def suffix(self) -> str:
        return self.path.suffix
    
    @property
    def display_name(self):
        return self.title
    
    @property
    def duration(self):
        return self.analysis.duration
    
    def base60_duration(self):
        return self.analysis.base60_duration
    
    def clear_analysis(self):
        self._analysis = None
    
#endregion
#region CACHE
    @property
    def cache_file(self) -> Path:
        return Path("cache") / f"{self.title}.json"
    
    def save_cache(self, analysis_dictionary: dict) -> None:
        cache_tools.save_song_cache(self.cache_file, analysis_dictionary)
    
    def load_cache(self) -> dict:
        return cache_tools.load_song_cache(self.cache_file)
    
#endregion