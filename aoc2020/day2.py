#!/usr/bin/env python3
"""
Day 2 - Advent of Code 2020
https://adventofcode.com/2020/day/2
"""

import re
import os

from .config import input_dir


def is_valid(pwd_and_policy):
    """ Takes a string representing a password and policy. They look like:

    1-3 a: abcde

    Returns True if valid; False if not
    """
    parser = re.compile(r'(\d+)-(\d+) ([a-z]): (\w+)')
    match = re.match(parser, pwd_and_policy)
    mini, maxi, char, pwd = match.groups()

    if int(mini) <= len(re.findall(char, pwd)) <= int(maxi):
        return True

    return False


def count_valid(pwd_list):
    """ Takes a list of password and policy strings.

    Returns a count of the valid passwords.
    """
    return len([x for x in pwd_list if is_valid(x)])

def run():
    """ Day 2 """
    print('DAY 2')
    print('-----')
    with open(os.path.join(input_dir, 'day2.txt'), 'r') as f:
        input_data = f.readlines()

        print(f'Part 1: {count_valid(input_data)}')
