from activities.time import extract_total_days, \
                            extract_total_hours, \
                            extract_total_minutes
from datetime import timedelta
import pytest


class TestExtractTotalDays(object):
    def test_less_than_one(self):
        td = timedelta(hours=12)
        actual = extract_total_days(td)
        expected = 1/2
        assert actual == pytest.approx(expected)
    def test_exactly_one(self):
        td = timedelta(hours=24)
        actual = extract_total_days(td)
        expected = 1
        assert actual == pytest.approx(expected)
    def test_more_than_one(self):
        td = timedelta(hours=48)
        actual = extract_total_days(td)
        expected = 2
        assert actual == pytest.approx(expected)


class TestExtractTotalHours(object):
    def test_less_than_one(self):
        td = timedelta(minutes=30)
        actual = extract_total_hours(td)
        expected = 1/2
        assert actual == pytest.approx(expected)
    def test_exactly_one(self):
        td = timedelta(minutes=60)
        actual = extract_total_hours(td)
        expected = 1
        assert actual == pytest.approx(expected)
    def test_more_than_one(self):
        td = timedelta(minutes=120)
        actual = extract_total_hours(td)
        expected = 2
        assert actual == pytest.approx(expected)


class TestExtractTotalMinutes(object):
    def test_less_than_one(self):
        td = timedelta(seconds=30)
        actual = extract_total_minutes(td)
        expected = 1/2
        assert actual == pytest.approx(expected)
    def test_exactly_one(self):
        td = timedelta(seconds=60)
        actual = extract_total_minutes(td)
        expected = 1
        assert actual == pytest.approx(expected)
    def test_more_than_one(self):
        td = timedelta(seconds=120)
        actual = extract_total_minutes(td)
        expected = 2
        assert actual == pytest.approx(expected)
