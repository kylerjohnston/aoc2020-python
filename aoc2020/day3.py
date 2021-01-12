#!/usr/bin/env python3
"""
Day 3, 2020
https://adventofcode.com/2020/day/3
"""

from functools import reduce
from operator import mul

from colorama import Fore, Style

class Map:
    """ A map of the local geology """
    def __init__(self, rows):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0])
        self.pos = {'x': 0, 'y': 0}

    def update_pos(self, x, y):
        """ Update position by x and y.
        If current position is (1,2) and x: 3, y: 1, the new position would
        be (4, 3).
        Returns False if it's reached the end of the map;
        otherwise returns True. """
        new_pos = {'x': self.pos['x'] + x, 'y': self.pos['y'] + y}
        if new_pos['y'] >= self.height:
            return False
        if new_pos['x'] >= self.width:
            new_pos['x'] = new_pos['x'] - self.width
        self.pos = new_pos
        return self.pos

    def is_tree(self, x, y):
        """ Return True if a given coordinate is a tree ('#'). Otherwise
        return False. """
        if self.rows[y][x] == '#':
            return True
        return False

    def print_pos(self):
        """ Print your current position. If the spot you occupy is empty
        print an O. If the spot has a tree, print an X. """
        current_pos = list(self.rows[self.pos['y']])
        if self.is_tree(self.pos['x'], self.pos['y']):
            current_pos[self.pos['x']] = Fore.RED + 'X' + Style.RESET_ALL
        else:
            current_pos[self.pos['x']] = Fore.GREEN + 'O' + Style.RESET_ALL

        print(''.join(current_pos))

    def find_trees_in_path(self, slope=(3, 1)):
        """ Given a slope, traverse the map and return the number of trees
        encountered. """
        x, y = slope
        trees = 0
        while True:
            if self.is_tree(self.pos['x'], self.pos['y']):
                trees += 1
            new_pos = self.update_pos(x, y)
            if not new_pos:
                self.pos = {'x': 0, 'y': 0}
                return trees
            self.print_pos()


def solve_part_1(input_data):
    """ Solve Part 1 """
    m = Map(input_data)
    return m.find_trees_in_path()


def solve_part_2(input_data):
    """ Part 2 """
    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]
    m = Map(input_data)
    trees_per_slope = [m.find_trees_in_path(slope=slope) for slope in slopes]
    return reduce(mul, trees_per_slope)
