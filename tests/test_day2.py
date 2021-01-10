#!/usr/bin/env python3

from aoc2020.day2 import is_valid, count_valid

day1_test_data = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"]

def test_day2_part1():
    assert is_valid("1-3 a: abcde")
    assert is_valid("2-9 c: ccccccccc")
    assert not is_valid("1-3 b: cdefg")
    assert count_valid(day1_test_data) == 2
