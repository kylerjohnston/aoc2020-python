#!/usr/bin/env python3

import argparse
import importlib
import os

from .config import input_dir

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2020 in Python')
    parser.add_argument('--days', type=int, nargs='+', help='Day number')
    args = parser.parse_args()

    for day in args.days:
        try:
            day_mod = importlib.import_module(f'.day{day}', package='aoc2020')
            day_str = f'DAY {day}'
            print('\n' + day_str)
            print('-' * len(day_str))
            with open(os.path.join(input_dir, f'day{day}.txt'), 'r') as f:
                input_data = f.readlines()
                print(f'Part 1: {day_mod.solve_part_1(input_data)}')
                print(f'Part 2: {day_mod.solve_part_2(input_data)}')
        except ModuleNotFoundError as e:
            print(f'\nNo program for day {day}.')
