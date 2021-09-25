
# activities

A super simple method for tracking usage of time for programmers.

## Usage

### Add activity

```
$ ./activities/app.py track
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

```
$ ./activities/app.py report
```
