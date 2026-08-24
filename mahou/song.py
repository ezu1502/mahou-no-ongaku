from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Song:

    id: int
    path: Path
    custom_title: str | None = None

    metadata: SongMetadata | None = None

    @property
    def title(self):
        if self.custom_title:
            return self.custom_title

        return self.path.stem

    def has_metadata(self) -> bool:
        return self.metadata is not None

@dataclass
class SongMetadata:

    artist: str | None
    genre: str | None

    #TODO adicionar mais info
