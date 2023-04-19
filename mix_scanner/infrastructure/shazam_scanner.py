from application.scanner import Scanner, ScannedTrack
from dataclasses import dataclass
from pydub import AudioSegment
from shazamio import Shazam, Serialize


@dataclass
class ShazamScannerParameters:
    scan_every: int
    scan_for: int


default_shazam_scanner_parameters = ShazamScannerParameters(
    scan_every=30 * 1000,  # 30 seconds
    scan_for=5 * 1000,  # 5 seconds
)


class ShazamScanner(Scanner):
    def __init__(
        self, parameters: ShazamScannerParameters = default_shazam_scanner_parameters
    ):
        self.parameters = parameters
        self.shazam = Shazam()

    async def scan(self, song: AudioSegment) -> list[ScannedTrack]:
        track_ids: set[int] = set()
        tracks: list[ScannedTrack] = []

        for cursor in range(0, len(song), self.parameters.scan_every):
            segment = song[cursor : cursor + self.parameters.scan_for]
            result = await self.shazam.recognize_song(segment)
            track = result.get("track")
            if track is not None and track.get("key") not in track_ids:
                track_id = track.get("key")
                track_ids.add(track_id)
                track_about_raw = await self.shazam.track_about(track_id)
                track_about = Serialize.track(data=track_about_raw)
                tracks.append(
                    ScannedTrack(
                        timestamp=cursor,
                        title=track_about.title,
                        artist=track_about.subtitle,
                    )
                )

        return tracks
