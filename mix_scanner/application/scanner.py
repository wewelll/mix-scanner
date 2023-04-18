from abc import ABC, abstractmethod
from pydub import AudioSegment
from dataclasses import dataclass


@dataclass
class ScannedTrack:
    timestamp: int
    title: str
    artist: str


class Scanner(ABC):
    @abstractmethod
    async def scan(self, audio: AudioSegment) -> list[ScannedTrack]:
        pass
