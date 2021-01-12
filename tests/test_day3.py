#!/usr/bin/env python3

from aoc2020.day3 import Map, solve_part_1, solve_part_2

day3_test_data = ['..##.......',
                  '#...#...#..',
                  '.#....#..#.',
                  '..#.#...#.#',
                  '.#...##..#.',
                  '..#.##.....',
                  '.#.#.#....#',
                  '.#........#',
                  '#.##...#...',
                  '#...##....#',
                  '.#..#...#.#']

def test_day3_part1():
    m = Map(day3_test_data)
    assert m.find_trees_in_path() == 7
    assert solve_part_1(day3_test_data) == 7


def test_day3_part_2():
    assert solve_part_2(day3_test_data) == 336
