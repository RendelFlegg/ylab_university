import unittest
from datetime import datetime

from homework_2 import CyclicIterator, Movie


class TestHomework2(unittest.TestCase):
    def test_cyclic_iterator(self):
        test_iter = CyclicIterator(['one', 'two', 'three'])
        test_list = []
        for _ in range(6):
            test_list.append(next(test_iter))
        self.assertTrue(test_list == ['one', 'two', 'three'] * 2, 'Error when iterating list')

        test_iter = CyclicIterator((1, 2, 3, 4))
        test_list = []
        for _ in range(5):
            test_list.append(next(test_iter))
        self.assertTrue(test_list == [1, 2, 3, 4, 1], 'Error when iterating tuple')

        test_iter = CyclicIterator(range(5))
        test_list = []
        for _ in range(16):
            test_list.append(next(test_iter))
        self.assertTrue(test_list[-1] == 0 and len(test_list) == 16, 'Error when iterating range')

    def test_movie(self):
        m = Movie('sw', [
            (datetime(2020, 1, 1), datetime(2020, 1, 7)),
            (datetime(2020, 1, 15), datetime(2020, 2, 7))
        ])
        counter = 0
        for _ in m.schedule():
            counter += 1
        self.assertEqual(counter, 31, 'Error with [01.01 - 01.07, 01.15 - 02.07]')

        m = Movie('sw', [
            (datetime(2020, 1, 1), datetime(2020, 1, 7))
        ])
        counter = 0
        for _ in m.schedule():
            counter += 1
        self.assertEqual(counter, 7, 'Error with [01.01 - 01.07]')

        m = Movie('sw', [
            (datetime(2020, 1, 1), datetime(2020, 1, 7)),
            (datetime(2020, 1, 15), datetime(2020, 2, 7)),
            (datetime(2020, 3, 10), datetime(2020, 3, 16))
        ])
        counter = 0
        for _ in m.schedule():
            counter += 1
        self.assertEqual(counter, 38, 'Error with [01.01 - 01.07, 01.15 - 02.07, 03.10 - 03.16]')

        m = Movie('sw', [
            (datetime(2020, 1, 1), datetime(2020, 1, 1))
        ])
        counter = 0
        for _ in m.schedule():
            counter += 1
        self.assertEqual(counter, 1, 'Error with [01.01 - 01.01]')
