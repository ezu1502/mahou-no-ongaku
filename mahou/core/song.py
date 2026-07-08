from dataclasses import dataclass
from pathlib import Path

#Cada música vai ser uma class agora

@dataclass
class Song:
    path: Path

    @property
    def title(self) -> str:
        return self.path.stem
    
    @property
    def suffix(self) -> str:
        return self.path.suffix
    
    @property
    def display_name(self):
        return self.title
    
    