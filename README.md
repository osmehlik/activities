
# activities

A simple command line time tracker.

## Installation

```
pip install .
```

## Usage

### Track a new activity

To track a new activity, run:

```
activities-cli track
```

It starts interactive dialog which looks like this:

```
activity name? studying
activity studying started
press enter to finish
activity studying finished
```

and generates `activities.csv` with content of this form:

```
started,finished,activity
2020-12-13 13:31:24,2020-12-13 15:12:42,studying
```

Running it more times just appends lines to this csv.

### Show an activities report

To show total time spent on different activities, run:

```
activities-cli report
```

By default it shows report sorted by length, descending
(= most time wasters first).

You can sort report output with `-s` *METHOD*, where *METHOD* is one of:

- `aa` - sort by activity, ascending
- `ad` - sort by activity, descending
- `la` - sort by length, ascending
- `ld` - sort by length, descending

So, to show report sorted by activity, ascending, run:

```
activities-cli report -s aa
```

## Uninstallation

```
pip uninstall activities
```
