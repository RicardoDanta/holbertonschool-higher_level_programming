#!/usr/bin/python3
"""unittests for the function max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing the Class"""

    def test_max_integer_end(self):
        self.assertEqual(max_integer([5, 3, 6]), 6)

    def test_max_integer_beggining(self):
        self.assertEqual(max_integer([6, 5, 3]), 6)

    def test_max_integer_middle(self):
        self.assertEqual(max_integer([6, 7, 5]), 7)

    def test_negative_number(self):
        self.assertEqual(max_integer([-5, 3, 6]), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -6, -7]), -5)

    def test_list_element(self):
        self.assertEqual(max_integer([6]), 6)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)
