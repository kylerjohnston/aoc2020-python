#!/usr/bin/env python3

import os
from aoc2020.config import input_dir
from aoc2020.day4 import (split_passports,
                          fields_present,
                          solve_part_1,
                          validate_field,
                          validate_passport,
                          solve_part_2)

with open(os.path.join(input_dir, 'day4_test.txt'), 'r') as f:
    day4_test_data = [line.strip() for line in f.readlines()]

part2_invalid_data = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".split('\n')

part2_valid_data = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""".split('\n')

def test_part1():
    passports = split_passports(day4_test_data)
    assert len(passports) == 4
    assert fields_present(passports[0])
    assert not fields_present(passports[1])
    assert fields_present(passports[2])
    assert not fields_present(passports[3])
    assert solve_part_1(day4_test_data) == 2


def test_byr():
    assert validate_field('byr:2002')
    assert not validate_field('byr:2003')


def test_hcl():
    assert validate_field('hcl:#123abc')
    assert not validate_field('hcl:#123abz')
    assert not validate_field('hcl:123abc')


def test_hgt():
    assert validate_field('hgt:60in')
    assert validate_field('hgt:190cm')
    assert not validate_field('hgt:190in')
    assert not validate_field('hgt:190')


def test_ecl():
    assert validate_field('ecl:brn')
    assert not validate_field('ecl:wat')


def test_pid():
    assert validate_field('pid:000000001')
    assert not validate_field('pid:0123456789')


def test_part2_invalid():
    passports = split_passports(part2_invalid_data)
    for passport in passports:
        assert not validate_passport(passport)


def test_part2_valid():
    passports = split_passports(part2_valid_data)
    for passport in passports:
        assert validate_passport(passport)

def test_part2():
    passports = part2_invalid_data + [''] + part2_valid_data
    assert solve_part_2(passports) == 4
