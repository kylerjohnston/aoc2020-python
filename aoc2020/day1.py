#!/usr/bin/env python3

import os

from functools import reduce
from operator import mul

from .config import input_dir

def find_addend_to_sum_to_num(term1, terms, total=2020):
    """
    Given a term (integer) and a list of terms, find the other term in the list
    of terms to satisfy:

    term + ____ = total

    Returns an integer
    """
    assert isinstance(term1, int)
    assert isinstance(terms, list)
    assert isinstance(total, int)

    matches = [x for x in terms if total - x == term1]
    if len(matches) < 1:
        return None
    return matches[0]


def find_terms_adding_to_num(terms, total=2020):
    """
    Given a list of `terms`, find the two that add to `total`

    Returns a tuple of integers
    """
    assert isinstance(terms, list)
    assert isinstance(total, int)

    lower = [x for x in terms if x <= total / 2]
    upper = [x for x in terms if x > total / 2]
    half = [x for x in lower if x == total / 2]

    if len(half) == 2:
        return (half[0], half[1])

    for term in lower:
        match = find_addend_to_sum_to_num(term, upper, total=2020)
        if match:
            return (term, match)

    return (None, None)

def solve_part_2(terms, total=2020):
    term1 = terms.pop()
    working_terms = list(terms)
    while len(working_terms) > 0:
        term2 = working_terms.pop()
        if term1 + term2 < total:
            match = find_addend_to_sum_to_num(term1 + term2, working_terms,
                                              total=total)
            if match:
                return (term1, term2, match)

    return solve_part_2(terms, total=total)


def run():
    """ Day 1 Part 1 """
    print('DAY 1')
    print('-----')
    with open(os.path.join(input_dir, 'day1.txt'), 'r') as f:
        input_data = [int(x) for x in f.readlines()]

        print('Part 1: ', end='')
        part1_terms = find_terms_adding_to_num(input_data, total=2020)
        print(part1_terms[0] * part1_terms[1])

        part2_terms = solve_part_2(input_data, total=2020)
        print(f'Part 2: {reduce(mul, part2_terms)}')
