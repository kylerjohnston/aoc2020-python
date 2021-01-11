#!/usr/bin/env python3
"""
Day 1 - Advent of Code 2020
https://adventofcode.com/2020/day/1
"""

import os

from functools import reduce
from operator import mul


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
    terms = [int(x) for x in terms]
    return reduce(mul, find_terms_adding_to_x(terms, n=n, total=total))


def solve_part_1(input_data):
    """ Part 1 """
    return solve(input_data, n=2)


def solve_part_2(input_data):
    """ Part 2"""
    return solve(input_data, n=3)
