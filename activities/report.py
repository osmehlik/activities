from activities.constants import DEFAULT_DATETIME_FORMAT, \
                                 DEFAULT_SORT_BY, \
                                 DEFAULT_TIMEDELTA_FORMAT
from activities.time import *
from datetime import datetime
import csv
import os
import sys


def report(path,
           sort_by=DEFAULT_SORT_BY,
           timedelta_fmt=DEFAULT_TIMEDELTA_FORMAT):
    """Shows activity report from file"""

    if not os.path.exists(path):
        print("We cannot show a report from a file that does not exist")
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
    if sort_by == "aa":  # activity ascending
        activities = sorted(activities, key=lambda row: row[0], reverse=False)
    elif sort_by == "ad":  # activity descending
        activities = sorted(activities, key=lambda row: row[0], reverse=True)
    elif sort_by == "la":  # length ascending
        activities = sorted(activities, key=lambda row: row[1], reverse=False)
    elif sort_by == "ld":  # length descending
        activities = sorted(activities, key=lambda row: row[1], reverse=True)
    else:
        print("Unknown sort_by value")
        sys.exit(1)

    # Prepare functions to describe activity
    def describe_activity(activity):
        return activity.rjust(activity_max_len, " ")

    supported_timedelta_fmts = set(["python-default", "td", "th", "tm"])

    # Error on unknown format
    if timedelta_fmt not in supported_timedelta_fmts:
        print("Unknown time length format")
        sys.exit(1)

    # Prepare functions to describe length
    if timedelta_fmt == "python-default":
        describe_length = str
    else:
        timedelta_value_extractors = {
            "td": extract_total_days,
            "th": extract_total_hours,
            "tm": extract_total_minutes
        }

        def describe_length(td):
            return "{0:.2f}".format(
                timedelta_value_extractors[timedelta_fmt](td)
            )

    # Print activities and lengths
    for activity, length in activities:
        print(describe_activity(activity), describe_length(length))
