from dataclasses import dataclass
from pathlib import Path
from mahou_libs.bocca import BoccaFiglia

log = BoccaFiglia("Song_Class", "#00FF00")

@dataclass
class Song:
    id: int
    path: Path
    title_: str

    @property
    def title(self):
        name = self.path.stem
        name = name.replace("\ufeff", "")
        return name


        

        








#endregion