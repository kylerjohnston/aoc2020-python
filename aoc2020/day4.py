#!/usr/bin/env python3
"""
Day 4
https://adventofcode.com/2020/day/4
"""

import re


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


def fields_present(passport):
    """ `passport` is a list where each field:value pair has been split into
    its own item.

    Returns True if the passport has all required fields, otherwise False """
    fields = [x.split(':')[0] for x in passport]
    if len(fields) == 8:
        return True

    if len(fields) == 7 and 'cid' not in fields:
        return True

    return False


def between(num, sm, lg):
    """ Given an integer `num`, return True if it is greater than or equal to
    `sm` and less than or equal to `lg`. """
    try:
        if int(num) >= sm and int(num) <= lg:
            return True
    except ValueError:
        pass
    return False


def validate_hgt(height):
    """ Given a height value, return True if valid, otherwise False """
    matches = re.match(r'^([\d]+)(in|cm)$', height)
    allowances = {'cm': [150, 193],
                  'in': [59, 76]}
    if matches:
        value, unit = matches.groups()
        if between(value, *allowances[unit]):
            return True
    return False


def validate_hcl(hcl):
    """ Give a hair color string `hcl`, return True if valid, else False """
    if re.match(r'^#[0-9a-f]{6}$', hcl):
        return True
    return False


def validate_pid(pid):
    """ Given a passport ID `pid`, return True if valid """
    if re.match(r'^[0-9]{9}$', pid):
        return True
    return False


def validate_field(fvp):
    """ Takes a field-value-pair (`fvp`) string, like 'byr:2002'.

    Returns True if the field is valid; otherwise False """
    field, value = fvp.split(':')

    rules = {
        'byr': lambda x: between(x, 1920, 2002),
        'iyr': lambda x: between(x, 2010, 2020),
        'eyr': lambda x: between(x, 2020, 2030),
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': validate_pid,
        'cid': lambda x: True
    }

    try:
        return rules[field](value)
    except KeyError:
        return False


def validate_passport(passport):
    """ `passport` is a list where each field:value pair has been split into
    its own item.

    Returns True if the passport is valid, otherwise False """
    if not fields_present(passport):
        return False

    for fvp in passport:
        if not validate_field(fvp):
            return False

    return True


def solve_part_1(input_data):
    """ Part 1 """
    return len([x for x in split_passports(input_data) if fields_present(x)])


def solve_part_2(input_data):
    """ Part 2 """
    return len([x for x in split_passports(input_data) if validate_passport(x)])
