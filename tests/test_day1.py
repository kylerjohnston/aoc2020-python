#!/usr/bin/env python3

from functools import reduce
from operator import mul

from aoc2020.day1 import find_terms_adding_to_num, find_terms_adding_to_x

day1_test_data = [1721,
                  979,
                  366,
                  299,
                  675,
                  1456]

def test_day1_part1():
    terms = find_terms_adding_to_x(day1_test_data, n=2, total=2020)
    assert 299 in terms
    assert 1721 in terms
    assert terms[0] * terms[1] == 514579

def test_day1_part2():
    terms = find_terms_adding_to_x(day1_test_data, n=3, total=2020)
    assert 979 in terms
    assert 366 in terms
    assert 675 in terms
    assert reduce(mul, terms) == 241861950
