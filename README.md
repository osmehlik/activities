
# activities-cli

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

It shows report of this form:

```
     studying    134 hours 25 minutes
playing piano     16 hours  4 minutes
      running      5 hours 17 minutes
```

## Advanced usage

See [doc/advanced_usage.md](doc/advanced_usage.md).

## Developer usage

See [doc/developer_usage.md](doc/developer_usage.md).

## Uninstallation

```
pip uninstall activities
```
