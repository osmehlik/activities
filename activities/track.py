from activities.constants import DEFAULT_DATETIME_FORMAT
from datetime import datetime
import os


def track(path):
    """Adds activity to file"""
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("started,finished,activity\n")
    activity = input("activity name? ")
    started = datetime.now()
    print("activity {} started".format(activity))
    input("press enter to finish")
    finished = datetime.now()
    print("activity {} finished".format(activity))
    with open(path, "a") as f:
        f.write(
            "{},{},{}\n".format(
                started.strftime(DEFAULT_DATETIME_FORMAT),
                finished.strftime(DEFAULT_DATETIME_FORMAT),
                activity
            )
        )
