from dataclasses import dataclass
from pathlib import Path
from mahou_libs.bocca import BoccaFiglia

log = BoccaFiglia("Song_Class", "#00FF00")



@dataclass
class SongMetadata:
    artist: str | None = None
    album: str | None = None
    track_number: int | None = None
    genre: str | None = None
    date: str | None = None


@dataclass
class Song:

    id: int
    path: Path
    title_: str
    play_count: int
    listen_time: float
    metadata: SongMetadata | None = None


    @property
    def title(self):
        name = self.path.stem
        name = name.replace("\ufeff", "")
        return name

    def __eq__(self, compared: object) -> bool:
        if isinstance(compared, Song):
            return compared.id == self.id
        elif isinstance(compared, int):
            return compared == self.id

        return NotImplemented

    





    
    

        

        








#endregion