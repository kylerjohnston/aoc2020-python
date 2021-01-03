#!/usr/bin/env python3
"""
Day 1 - Advent of Code 2020
https://adventofcode.com/2020/day/1
"""

import os

from functools import reduce
from operator import mul

from .config import input_dir


def find_terms_adding_to_x(terms, n=2, total=2020):
    """ Given a list of integer `terms`, find the `n` terms that add
    to `total`

    Return those `n` terms as a tuple of integers.
    """
    if len(terms) == 0:
        return []

    if n == 1:
        if total in terms:
            return [total]
        return []

    working_terms = list(terms)
    term1 = working_terms.pop()
    remaining_terms = list(working_terms)
    matches = find_terms_adding_to_x(remaining_terms,
                                     n=n-1,
                                     total=total-term1)
    if matches:
        return [term1] + matches

    return find_terms_adding_to_x(working_terms, n=n, total=total)


def solve(terms, n=2, total=2020):
    """ Given a list of integer `terms`, find the `n` terms that add
    to `total` and return the product of those terms multiplied together """
    return reduce(mul, find_terms_adding_to_x(terms, n=n, total=total))


def run():
    """ Day 1 """
    print('DAY 1')
    print('-----')
    with open(os.path.join(input_dir, 'day1.txt'), 'r') as f:
        input_data = [int(x) for x in f.readlines()]

        print(f'Part 1: {solve(input_data, n=2, total=2020)}')
        print(f'Part 2: {solve(input_data, n=3, total=2020)}')
