from activities.constants import NUM_MINUTES_IN_HOUR, \
                                 NUM_SECONDS_IN_DAY, \
                                 NUM_SECONDS_IN_HOUR, \
                                 NUM_SECONDS_IN_MINUTE
from datetime import timedelta


def extract_total_days(td: timedelta) -> float:
    return td.total_seconds() / NUM_SECONDS_IN_DAY


def extract_total_hours(td: timedelta) -> float:
    return td.total_seconds() / NUM_SECONDS_IN_HOUR


def extract_total_minutes(td: timedelta) -> float:
    return td.total_seconds() / NUM_SECONDS_IN_MINUTE


def extract_hours_minutes(td: timedelta) -> (float, float):
    total_minutes = extract_total_minutes(td)
    return divmod(total_minutes, NUM_MINUTES_IN_HOUR)
