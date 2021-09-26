
# activities

A super simple method for tracking usage of time for programmers.

## Installation

```
pip install .
```

## Usage

### Track a new activity

```
$ activities-cli track
activity name? studying
activity studying started
press enter to finish
activity studying finished
```

Example usage would generate `activities.csv` with content of this form:

```
started,finished,activity
2020-12-13 13:31:24,2020-12-13 15:12:42,studying
```

### Show an activities report

To show total time spent on different activities, run:

```
$ activities-cli report
```

You can sort report output with `-s`*METHOD*, where *METHOD* is one of:

- `aa` - sort by activity, ascending
- `ad` - sort by activity, descending
- `la` - sort by length, ascending
- `ld` - sort by length, descending

So, to show report sorted by activity, ascending, run:

```
$ activities-cli report -saa
```

## Uninstallation

```
pip uninstall activities
```
