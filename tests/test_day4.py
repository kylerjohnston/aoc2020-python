#!/usr/bin/env python3

import os
from aoc2020.config import input_dir
from aoc2020.day4 import split_passports, validate_passport, solve_part_1

with open(os.path.join(input_dir, 'day4_test.txt'), 'r') as f:
    day4_test_data = [line.strip() for line in f.readlines()]

def test_part1():
    passports = split_passports(day4_test_data)
    assert len(passports) == 4
    assert validate_passport(passports[0])
    assert not validate_passport(passports[1])
    assert validate_passport(passports[2])
    assert not validate_passport(passports[3])
    assert solve_part_1(day4_test_data) == 2
