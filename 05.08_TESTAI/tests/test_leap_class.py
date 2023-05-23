import unittest
from leap import Keliamieji

class TestKeliamiejiClass(unittest.TestCase):
    def setUp(self):
        self.leap = Keliamieji()


    def test_check_method(self):
        self.assertFalse(self.leap.tikrinti(2100))
        self.assertTrue(self.leap.tikrinti(2000))


    def test_range_method(self):
        result = self.leap.diapazonas(1980,2000)
        self.assertEqual(result, [1980, 1984, 1988, 1992, 1996])