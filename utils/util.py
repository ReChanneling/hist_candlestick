def interval_to_minutes(interval: str) -> int:
    unit = interval[-1:]
    if unit == 'm':
        return int(interval[:-1])
    if unit == 's':
        return int(interval[:-1]) / 60
    if unit == 'h':
        return int(interval[:-1]) * 60
    if unit == 'd':
        return int(interval[:-1]) * 60 * 24
    if unit == 'w':
        return int(interval[:-1]) * 60 * 24 * 7
    return int(interval[:-1])