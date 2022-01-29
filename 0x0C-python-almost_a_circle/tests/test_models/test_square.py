#!/usr/bin/python3
"""test file for square"""


import unittest
from models.square import Square


class SquareTest(unittest.TestCase):
  """squaretest test testing"""

  def test_square(self):
    """squesting"""
    s1 = Square(1, 2, 3, 4)
    s2 = Square(1, 2)
    s3 = Square(1, 2, 3)
    s7 = Square(1, 2, 3, 4)
    s12 = s1.to_dictionary()
    self.assertEqual(s1.size, 1)
    self.assertEqual(s2.x, 2)
    self.assertEqual(s3.y, 3)
    with self.assertRaises(TypeError):
        s4 = Square("1")
    with self.assertRaises(TypeError):
        s5 = Square(1, "2")
    with self.assertRaises(TypeError):
        s6 = Square(1, 2, "3")
    self.assertEqual(s7.id, 4)
    with self.assertRaises(ValueError):
        s8 = Square(-1)
    with self.assertRaises(ValueError):
        s9 = Square(1, -2)
    with self.assertRaises(ValueError):
        s10 = Square(1, 2, -3)
    with self.assertRaises(ValueError):
        s11 = Square(0)
    self.assertEqual(s1.__str__(), "[Square] (4) 2/3 - 1")
    self.assertIsInstance(s12, dict)
    s1.update(89)
    self.assertEqual(s1.id, 89)
    s1.update(89, 1)
    self.assertEqual(s1.size, 1)
    s1.update(89, 1, 2)
    self.assertEqual(s1.x, 2)
    s1.update(89, 1, 2, 3)
    self.assertEqual(s1.y, 3)
    s1.update(**{'id': 89})
    self.assertEqual(s1.id, 89)
    s1.update(**{'id': 89, 'size': 1})
    self.assertEqual(s1.size, 1)
    s1.update(**{ 'id': 89, 'size': 1, 'x': 2})
    self.assertEqual(s1.x, 2)
    s1.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3})


  if __name__ == '__main__':
    unittest.main()