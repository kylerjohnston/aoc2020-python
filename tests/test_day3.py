#!/usr/bin/env python3

from aoc2020.day3 import Map

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
