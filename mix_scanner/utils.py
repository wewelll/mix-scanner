from application.scanner import ScannedTrack


def format_milliseconds(ms: int) -> str:
    seconds = (ms / 1000) % 60
    seconds = int(seconds)
    minutes = (ms / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (ms / (1000 * 60 * 60)) % 24

    return "%d:%d:%d" % (hours, minutes, seconds)


def format_track(track: ScannedTrack) -> str:
    return f"{track.artist} - {track.title} [{format_milliseconds(track.timestamp)}]"


def format_tracklist(tracklist: list[ScannedTrack]):
    return "\n".join([format_track(track) for track in tracklist])
