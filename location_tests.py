import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc1 = Location("San Diego", 106.54, 113.69)
        self.assertEqual(repr(loc1),"Location('San Diego', 106.54, 113.69)") 
        loc2 = Location("LA", 0, 180)
        self.assertEqual(repr(loc2),"Location('LA', 0, 180)")

    def test_eq_are_the_same(self):
        loc1 = Location("San Diego", 106.54, 113.69)
        loc3 = Location("San Diego", 106.54, 113.69)
        self.assertTrue(loc1 == loc3)

    def test_eq_have_dif_long(self):
        loc2 = Location("LA", 0, 180) 
        loc4 = Location("LA", 0, -180)
        self.assertFalse(loc2 == loc4)

    def test_eq_have_dif_lat(self):
        loc5 = Location("LA", 1, 180)
        loc2 = Location("LA", 0, 180)
        self.assertFalse(loc2 == loc5)

    def test_eq_have_dif_name(self):
        loc2 = Location("LA", 0, 180)
        loc6 = Location("la", 0, 180)
        loc7 = Location("SD", 0, 180)
        self.assertFalse(loc2 == loc6)
        self.assertFalse(loc2 == loc7)


if __name__ == "__main__":
        unittest.main()
