#!/usr/bin/env python3
"""
Day 4
https://adventofcode.com/2020/day/4
"""

def split_passports(passport_data):
    """ split passport data into lists of individual passports.

    Return a nested list where each sublist is an individual passport """
    # passports are separated by blank lines
    breaks = [i for i, x in enumerate(passport_data) if x == '']
    passports = []
    for i, x in enumerate(breaks):
        if i == 0:
            passports.append(passport_data[:x])
        else:
            passports.append(passport_data[breaks[i - 1] + 1:x])
    passports.append(passport_data[breaks[-1] + 1:])
    # Each field:value pair is its own item for each passport in the list
    return [' '.join(x).split(' ') for x in passports]


def validate_passport(passport):
    """ `passport` is a list where each field:value pair has been split into
    its own item.

    Returns True if the passport is valid, otherwise False """
    fields = [x.split(':')[0] for x in passport]
    if len(fields) == 8:
        return True

    if len(fields) == 7 and 'cid' not in fields:
        return True

    return False


def solve_part_1(input_data):
    """ Part 1 """
    return len([x for x in split_passports(input_data) if validate_passport(x)])


def solve_part_2(input_data):
    """ Part 2 """
    return "Not yet implemented"
