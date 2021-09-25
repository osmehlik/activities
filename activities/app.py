#!/usr/bin/env python3


from activities.constants import DEFAULT_DATABASE_PATH, DEFAULT_SORT_BY
from activities.track import track
from activities.report import report
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'action',
        help="one of: track/report"
    )
    parser.add_argument(
        '-f',
        help="path to file with activities",
        default=DEFAULT_DATABASE_PATH
    )
    parser.add_argument(
        '-s',
        help="when reporting, sort by, one of: aa/ad/la/ld",
        default=DEFAULT_SORT_BY
    )
    args = parser.parse_args()
    if args.action == "track":
        track(args.f)
    elif args.action == "report":
        report(args.f, sort_by=args.s)
    else:
        print("Unknown action")


if __name__ == "__main__":
    main()
