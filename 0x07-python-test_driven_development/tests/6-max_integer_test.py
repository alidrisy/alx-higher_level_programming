#!/usr/bin/python3
"""Unittest for max_integer ([..])"""


import unittest

max_integer import__('6-max_integer'). max_integer


class TestMaxInteger (unittest.TestCase):
	"""Define unittest for max_integer([..])"""
	def test_listInt(self):
		"""Test every case for list integer"""
        self.assertEqual(max_integer ([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 4, 6, 7]), 7)
        self.assertEqual(max_integer ([3, -4, 2, 5]), 5)
        self.assertEqual(max_integer ([-2, -4, -1, -6]), -1)
        self.assertEqual(max_integer (['2', '6' '3']), '6')
        self.assertEqual(max_integer ([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([]), None)

    def test_listFloat(self):
        """Test every case for list float"""

        self.assertEqual(max_integer ([2.4, 2.5, 1.8, 21]), 2.5)
        self.assertEqual (max_integer ([-1.4, 2.5, 1.8, -2]), -1.4)

    def test_tuple(self):
        """Test tuple"""
        self.assertEqual(max_integer((1, 6, 3)), 6)
        with self.assertRaises (TypeError):
            max_integer((1))

    def test_matrix(self):
        """Test matrix(list for list)"""
        matrix [
                [1, 2, 3],
                [0, 5, 9]
                ]
        self.assertEqual(max_integer (matrix), [1, 2, 3])
        matrix = [
                [1, 2, 3],
                [1, 5, 9]
                ]
        self.assertEqual(max_integer (matrix), [1, 5, 9])
    def test_string(self):
        """Test string and list of string"""
        self.assertEqual(max_integer("string"), "t")
        self.assertEqual(max_integer (['my','name', 'is', 'abdo']), 'name')
        self.assertEqual(max_integer(""), None)

    def test_raises(self):
        """Test raises errors"""
        with self.assertRaises (TypeError):
            max_integer(['4', 5, 2])

        with self.assertRaises (ValueError):
            max_integer([int('x'), 5, 2])

        with self.assertRaises (TypeError):
            max_integer ([None, 5, 2])
        with self.assertRaises (ValueError):
            max_integer([float('x'), 7, 5])

if__name__ == '__main__':
	unittest.main()



