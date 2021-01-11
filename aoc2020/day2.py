#!/usr/bin/env python3
"""
Day 2 - Advent of Code 2020
https://adventofcode.com/2020/day/2
"""

import re
import os


def is_valid(pwd_and_policy, policy='count'):
    """ Takes a string representing a password and policy, and a policy type
    which must be 'count' or 'positional'. Part 1 uses the 'count' policy,
    which counts occurances of a character in the password; Part 2 uses the
    positional policy, which looks at a character's position in the password.

    They look like:

    1-3 a: abcde

    Returns True if valid; False if not
    """
    assert policy in ['count', 'positional'], (
        "Policy must be 'count' or 'positional'")

    parser = re.compile(r'(\d+)-(\d+) ([a-z]): (\w+)')
    match = re.match(parser, pwd_and_policy)
    p1, p2, char, pwd = match.groups()

    p1 = int(p1)
    p2 = int(p2)

    if policy == 'count':
        if p1 <= len(re.findall(char, pwd)) <= p2:
            return True

    elif policy == 'positional':
        positions = [x for x in [pwd[p1-1], pwd[p2-1]] if x == char]
        if len(positions) == 1:
            return True

    return False


def count_valid(pwd_list, policy='count'):
    """ Takes a list of password and policy strings.

    Returns a count of the valid passwords.
    """
    return len([x for x in pwd_list if is_valid(x, policy=policy)])


def solve_part_1(input_data):
    """ Part 1"""
    return count_valid(input_data)


def solve_part_2(input_data):
    """ Part 2"""
    return count_valid(input_data, policy='positional')
