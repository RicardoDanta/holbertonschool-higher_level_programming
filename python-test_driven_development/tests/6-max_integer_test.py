#!/usr/bin/python3
"""Test"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Testing the Class"""
    def max_integer_end(self):
        self.assertEqual(max_integer([5, 6]), 6)

    def max_integer_beggining(self):
        self.assertEqual(max_integer([6, 5]), 6)

    def max_integer_middle(self):
        self.assertEqual(max_integer([6, 7, 5]), 7)

    def negative_number(self):
        self.assertEqual(max_integer([-5, 6]), 6)

    def negative_numbers(self):
        self.assertEqual(max_integer([-5, -6]), -5)

    def list_element(self):
        self.assertEqual(max_integer([6]), 6)

    def list_empty(self):
        self.assertEqual(max_integer([]), None)
