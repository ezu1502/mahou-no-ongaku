from dataclasses import dataclass, field
from pathlib import Path
from bunseki import Analyzer
from mahou.core import cache_tools
from mahou.core.cache_tools import CacheDoppelganger
from functools import wraps
from mahou_libs import mahou_math
from send2trash import send2trash
import logging
from mahou_libs import painted_string

#Cada música vai ser uma class agora
log = logging.getLogger(painted_string("Song_Class", "#00FF00"))

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
    
    @property
    def properties(self):
        properties = self.analysis.properties
        if properties is not None:
            return properties
        return None
    

    def load_properties(self):
        properties = self.properties
        if properties is None:
            self.analysis.load_heavy_analysis()
            
        


    @property
    def cache(self):
        cache_dict = self.cache_dict
        if self.properties is not None or cache_dict is None:
            return None
        return CacheDoppelganger(duration = cache_dict["duration_seconds"])
    
    @property
    def has_cache(self):
        cache_dict = self.cache_dict
        return (cache_dict is not None)
    
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
    def _properties_or_cache(self):
        properties = self.properties
        cache = self.cache

        if properties is not None:
            log.debug("Bunseki analysis used")
            return properties
        elif cache is not None:
            log.debug("cache used")
            return cache
        
        raise RuntimeError("Both analysis and cache were none, couldn't complete request"
        "\n maybe you forgot loading heavy analysis?")

    @property
    def duration(self) -> int | float:
        return self.analysis.duration # type: ignore
        
    @property
    def base60_duration(self):
        return mahou_math.conversions.seconds_to_base60(self.duration)
            
    def undo_heavy_analysis(self):
        self.analysis.properties = None
    
#endregion
#region CACHE
    @property
    def cache_file(self) -> Path:
        return Path ("mahou_cache") / ("song_cache") / f"{self.title}.json"
    
    def save_cache(self, analysis_dictionary: dict) -> None:
        cache_tools.save_song_cache(self.cache_file, analysis_dictionary)

    def save_analyzer_data_cache(self):
        if self.properties is not None:
            self.save_cache(self.analysis.get_analysis_dictionary())
            log.info(f"{self.title} cache generated!")
    
    @property
    def cache_dict(self) -> dict | None:
        cache = cache_tools.load_song_cache(self.cache_file)
        return cache if cache is not None else None
    
    def clear_own_cache(self) -> None:
        if self.cache_file.suffix.lower() == ".json":
            send2trash(self.cache_file)
        


        
#TODO TERMINAR ANÁLISE DO BUNSEKI E IMPLEMENTAR AQUI!


        

        








#endregion