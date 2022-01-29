#!/usr/bin/python3
"""test file for rectangle"""


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

    def test_recterror(self):
        "recterrifying"
        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2, 3, 4)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2", 3, 4)
        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, "3", 4)
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, "4")

    def test_toomany(self):
        """too many cooks"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r8 = Rectangle(1, 1)
        r9 = Rectangle(1, 1, 0)
        r10 = r1.to_dictionary()
        self.assertEqual(r1.id, 5)
        with self.assertRaises(ValueError):
            r2 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r7 = Rectangle(1, 2, 3, -4)
        self.assertEqual(r1.area(), 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(r8.display(), None)
        self.assertEqual(r9.display(), None)
        self.assertIsInstance(r10, dict)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 1)
        self.assertEqual(r1.width, 1)
        r1.update(89, 1, 2)
        self.assertEqual(r1.height, 2)
        r1.update(89, 1, 2, 3)
        self.assertEqual(r1.x, 3)
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.y, 4)
        r1.update(**{'id': 89})
        self.assertEqual(r1.id, 89)
        r1.update(**{'id': 89, 'width': 1})
        self.assertEqual(r1.width, 1)
        r1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.height, 2)
        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.x, 3)
        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.y, 4)

    if __name__ == '__main__':
        unittest.main()
