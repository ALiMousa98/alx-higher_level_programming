#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case class for max_integer function"""

    def test_positive_numbers(self):
        """Test case for positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([9, 7, 2, 5]), 9)
    
    def test_negative_numbers(self):
        """Test case for negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-9, -7, -2, -5]), -2)
    
    def test_mixed_numbers(self):
        """Test case for mixed positive and negative numbers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)
        self.assertEqual(max_integer([-9, 7, -2, 5]), 7)
    
    def test_single_element(self):
        """Test case for a single-element list"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([0]), 0)
    
    def test_empty_list(self):
        """Test case for an empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_duplicates(self):
        """Test case for a list with duplicate numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-3, -3, -3]), -3)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
