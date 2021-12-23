from activities.constants import DEFAULT_DATETIME_FORMAT, \
                                 DEFAULT_SORTING_METHOD, \
                                 DEFAULT_TIMEDELTA_FORMAT, \
                                 SUPPORTED_SORTING_METHODS, \
                                 SUPPORTED_TIMEDELTA_FORMATS
from activities.time import *
from datetime import datetime
import csv
import os
import sys


def report(path,
           sorting_method=DEFAULT_SORTING_METHOD,
           timedelta_format=DEFAULT_TIMEDELTA_FORMAT):
    """Shows activity report from file"""

    err_msg_begin = "To show activity report, you should specify"

    if not os.path.exists(path):
        print(err_msg_begin, "a path to existing file :)")
        sys.exit(1)

    if sorting_method not in SUPPORTED_SORTING_METHODS:
        print(err_msg_begin, "a supported sorting method :)")
        sys.exit(1)

    if timedelta_format not in SUPPORTED_TIMEDELTA_FORMATS:
        print(err_msg_begin, "a supported timedelta format :)")
        sys.exit(1)

    # Populate activity_to_length, which is
    # map of activity name to total time spent on that activity
    activity_to_length = {}

    activity_max_len = 0
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            started = datetime.strptime(
                row["started"],
                DEFAULT_DATETIME_FORMAT
            )
            finished = datetime.strptime(
                row["finished"],
                DEFAULT_DATETIME_FORMAT
            )
            activity = row["activity"]
            length = finished - started
            if activity in activity_to_length:
                activity_to_length[activity] += length
            else:
                activity_to_length[activity] = length
            activity_len = len(activity)
            if activity_len > activity_max_len:
                activity_max_len = activity_len

    # Convert dict to list
    activities = list(activity_to_length.items())

    # Sort list of activities
    if sorting_method == "aa":  # activity ascending
        activities.sort(key=lambda row: row[0], reverse=False)
    elif sorting_method == "ad":  # activity descending
        activities.sort(key=lambda row: row[0], reverse=True)
    elif sorting_method == "la":  # time ascending
        activities.sort(key=lambda row: row[1], reverse=False)
    elif sorting_method == "ld":  # time descending
        activities.sort(key=lambda row: row[1], reverse=True)

    # Prepare functions to describe activity
    def describe_activity(activity):
        return activity.rjust(activity_max_len, " ")

    # Prepare functions to describe length
    if timedelta_format == "str":
        describe_length = str
    elif timedelta_format == "hm":
        def describe_length(td):
            hours, minutes = extract_hours_minutes(td)
            return "{:6.0f} hours {:2.0f} minutes".format(hours, minutes)
    else:
        timedelta_value_extractors = {
            "d": extract_total_days,
            "h": extract_total_hours,
            "m": extract_total_minutes
        }

        def describe_length(td):
            return "{:6.2f}".format(
                timedelta_value_extractors[timedelta_format](td)
            )

    # Print activities and lengths
    for activity, length in activities:
        print(describe_activity(activity), describe_length(length))
