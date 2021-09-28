from activities.constants import DATETIME_FORMAT, \
                                 DEFAULT_SORT_BY, \
                                 DEFAULT_TIMEDELTA_FORMAT
from activities.time_extractors import *
from datetime import datetime
import csv
import sys


def report(path,
           sort_by=DEFAULT_SORT_BY,
           timedelta_fmt=DEFAULT_TIMEDELTA_FORMAT):
    """Shows activity report from file"""

    # Populate activity_to_length, which is
    # map of activity name to total time spent on that activity
    activity_to_length = {}

    activity_max_len = 0
    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            started = datetime.strptime(row[0], DATETIME_FORMAT)
            finished = datetime.strptime(row[1], DATETIME_FORMAT)
            activity = row[2]
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

    # Prepare functions to describe length
    if timedelta_fmt == "python-default":
        describe_length = str
    elif timedelta_fmt == "td":
        describe_length = extract_total_days_str
    elif timedelta_fmt == "th":
        describe_length = extract_total_hours_str
    elif timedelta_fmt == "tm":
        describe_length = extract_total_minutes_str

    # Print activities and lengths
    for activity, length in activities:
        print(describe_activity(activity), describe_length(length))
