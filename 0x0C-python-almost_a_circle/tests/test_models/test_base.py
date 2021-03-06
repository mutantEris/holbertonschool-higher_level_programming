#!/usr/bin/python3
"""test file for base"""


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """basetest test testing"""

    def test_id(self):
        """stringle"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_ids(self):
        """stringles"""
        b1 = Base(15)
        self.assertEqual(b1.id, 15)  

    def test_base_to_json(self):
        """base to json"""
        b1 = Base(1)
        self.assertEqual(b1.to_json_string(None), '[]')
        self.assertEqual(b1.to_json_string([]), '[]')
        self.assertEqual(b1.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
    
        
    if __name__ == '__main__':
        unittest.main()