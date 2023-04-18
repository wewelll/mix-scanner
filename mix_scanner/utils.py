def format_milliseconds(ms: int) -> str:
    seconds = (ms / 1000) % 60
    seconds = int(seconds)
    minutes = (ms / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (ms / (1000 * 60 * 60)) % 24

    return "%d:%d:%d" % (hours, minutes, seconds)
