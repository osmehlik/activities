
# activities - advanced usage

## How to specify path to csv file to work on

You can specify path to csv file containing activities:

```
activities-cli track -f path_to_some.csv
activities-cli report -f path_to_some.csv
```

## How to sort activities report

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
