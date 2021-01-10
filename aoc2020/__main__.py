#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2020 in Python')
    parser.add_argument('--days', type=int, nargs='+', help='Day number')
    args = parser.parse_args()

    for day in args.days:
        if day == 1:
            from . import day1
            day1.run()
        elif day == 2:
            from . import day2
            day2.run()
