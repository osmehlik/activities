#!/usr/bin/env python3


from activities.constants import DEFAULT_DATABASE_PATH, \
                                 DEFAULT_SORTING_METHOD, \
                                 DEFAULT_TIMEDELTA_FORMAT
from activities.track import track
from activities.report import report
import argparse


def make_parser():
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
        default=DEFAULT_SORTING_METHOD
    )
    parser.add_argument(
        "-l",
        help="when reporting, how to format time lengths, "
             "one of: str/d/h/m/hm",
        default=DEFAULT_TIMEDELTA_FORMAT
    )
    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()
    if args.action == "track":
        track(args.f)
    elif args.action == "report":
        report(args.f, sorting_method=args.s, timedelta_format=args.l)
    else:
        print("To do an action, you should specify a supported one :)")
        sys.exit(1)


if __name__ == "__main__":
    main()
