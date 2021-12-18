from activities.constants import NUM_SECONDS_IN_DAY, \
                                 NUM_SECONDS_IN_HOUR, \
                                 NUM_SECONDS_IN_MINUTE
from datetime import timedelta


def extract_total_days(td: timedelta) -> float:
    return td.total_seconds() / NUM_SECONDS_IN_DAY


def extract_total_hours(td: timedelta) -> float:
    return td.total_seconds() / NUM_SECONDS_IN_HOUR


def extract_total_minutes(td: timedelta) -> float:
    return td.total_seconds() / NUM_SECONDS_IN_MINUTE


def extract_total_days_str(td: timedelta) -> str:
    value = extract_total_days(td)
    return "{0:.2f}".format(value)


def extract_total_hours_str(td: timedelta) -> str:
    value = extract_total_hours(td)
    return "{0:.2f}".format(value)


def extract_total_minutes_str(td: timedelta) -> str:
    value = extract_total_minutes(td)
    return "{0:.0f}".format(value)
