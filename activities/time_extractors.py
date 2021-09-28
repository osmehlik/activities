from datetime import timedelta


NUM_SECONDS_IN_MINUTE = 60
NUM_MINUTES_IN_HOUR = 60
NUM_HOURS_IN_DAY = 24
NUM_SECONDS_IN_HOUR = NUM_MINUTES_IN_HOUR * NUM_SECONDS_IN_MINUTE
NUM_SECONDS_IN_DAY = NUM_HOURS_IN_DAY * NUM_SECONDS_IN_HOUR


def extract_total_days_value(td: timedelta) -> float:
    return int(td.total_seconds()) / NUM_SECONDS_IN_DAY


def extract_total_hours_value(td: timedelta) -> float:
    return int(td.total_seconds()) / NUM_SECONDS_IN_HOUR


def extract_total_minutes_value(td: timedelta) -> float:
    return int(td.total_seconds()) / NUM_SECONDS_IN_MINUTE


def extract_total_days_str(td: timedelta) -> str:
    value = extract_total_days_value(td)
    return "{0:.2f}".format(value)


def extract_total_hours_str(td: timedelta) -> str:
    value = extract_total_hours_value(td)
    return "{0:.2f}".format(value)


def extract_total_minutes_str(td: timedelta) -> str:
    value = extract_total_minutes_value(td)
    return "{0:.0f}".format(value)
