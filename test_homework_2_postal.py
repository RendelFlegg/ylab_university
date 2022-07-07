import unittest
import math

import homework_2_postal


class TestHomework2Postal(unittest.TestCase):
    def test_find_distance(self):
        self.assertEqual(homework_2_postal.find_distance((0, 0), (0, 0)), 0,
                         'Error when checking "(0, 0), (0, 0)"')
        self.assertEqual(homework_2_postal.find_distance((1, 0), (0, 0)), 1,
                         'Error when checking "(1, 0), (0, 0)"')
        self.assertEqual(homework_2_postal.find_distance((0, 1), (0, 0)), 1,
                         'Error when checking "(0, 1), (0, 0)"')
        self.assertEqual(homework_2_postal.find_distance((0, 0), (1, 0)), 1,
                         'Error when checking "(0, 0), (1, 0)"')
        self.assertEqual(homework_2_postal.find_distance((0, 0), (0, 1)), 1,
                         'Error when checking "(0, 0), (0, 1)"')
        self.assertEqual(homework_2_postal.find_distance((-1, 0), (0, 0)), 1,
                         'Error when checking "(-1, 0), (0, 0)"')
        self.assertEqual(homework_2_postal.find_distance((0, 0), (0, -1)), 1,
                         'Error when checking "(0, 0), (0, -1)"')
        self.assertEqual(homework_2_postal.find_distance((2, 0), (1, 0)), 1,
                         'Error when checking "(2, 0), (1, 0)"')
        self.assertEqual(homework_2_postal.find_distance((1, 0), (0, 1)), 1.4142135623730951,
                         'Error when checking "(1, 0), (0, 1)"')
        self.assertEqual(homework_2_postal.find_distance((1, 1), (0, 0)), 1.4142135623730951,
                         'Error when checking "(1, 1), (0, 0)"')
        self.assertEqual(homework_2_postal.find_distance((0, 1), (1, 4)), 3.1622776601683795,
                         'Error when checking "(0, 1), (1, 4)"')

    def test_find_total_distance(self):
        self.assertEqual(homework_2_postal.find_total_distance([(0, 0), (0, 0)]), 0,
                         'Error when checking "[(0, 0), (0, 0)]"')
        self.assertEqual(homework_2_postal.find_total_distance([(0, 0), (0, 0), (0, 0)]), 0,
                         'Error when checking "[(0, 0), (0, 0), (0, 0)]"')
        self.assertEqual(homework_2_postal.find_total_distance([(0, 0), (0, 0), (1, 0)]), 1,
                         'Error when checking "[(0, 0), (0, 0), (1, 0)]"')
        self.assertEqual(homework_2_postal.find_total_distance([(0, 0), (1, 0), (1, 0)]), 1,
                         'Error when checking "[(0, 0), (1, 0), (1, 0)]"')
        self.assertEqual(homework_2_postal.find_total_distance([(0, 0), (1, 0), (0, 0)]), 2,
                         'Error when checking "[(0, 0), (1, 0), (0, 0)]"')
        self.assertEqual(homework_2_postal.find_total_distance([(0, 0), (1, 0), (-1, 0)]), 3,
                         'Error when checking "[(0, 0), (1, 0), (-1, 0)]"')
        self.assertEqual(homework_2_postal.find_total_distance([(0, 0), (1, 0), (0, 1)]), 2.414213562373095,
                         'Error when checking "[(0, 0), (1, 0), (0, 1)]"')

    def test_find_get_combinations(self):
        self.assertTrue(len(set(homework_2_postal.get_combinations(['A', 'B']))) == math.factorial(2),
                        'Error when checking ["A", "B"]')
        self.assertTrue(len(set(homework_2_postal.get_combinations(['A', 'B', 'C']))) == math.factorial(3),
                        'Error when checking ["A", "B", "C"]')
        self.assertTrue(len(set(homework_2_postal.get_combinations(['A', 'B', 'C', 'D']))) == math.factorial(4),
                        'Error when checking ["A", "B", "C", "D"]')
        self.assertTrue(len(set(homework_2_postal.get_combinations(['A', 'B', 'C', 'D', 'E']))) == math.factorial(5),
                        'Error when checking ["A", "B", "C", "D", "E"]')
