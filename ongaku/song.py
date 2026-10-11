from dataclasses import dataclass
from pathlib import Path

@dataclass
class Song:
    path: Path

    play_count: float
    listen_time: float

    custom_title: str | None = None



    @property
    def title(self) -> str:
        return self.custom_title or self.path.stem