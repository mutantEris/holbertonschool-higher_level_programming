#!/usr/bin/python3
"""test file for base"""


import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    """rectangletest test testing"""

    def test_rectangle(self):
        """rectesting"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)


    if __name__ == '__main__':
        unittest.main()