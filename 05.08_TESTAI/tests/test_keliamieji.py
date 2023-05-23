import unittest
from keliamieji import is_leap

class TestIsLeap(unittest.TestCase):

    def test_is_leap_true(self):
        self.assertTrue(is_leap(2000))


    def test_is_leap_false(self):
        self.assertFalse(is_leap(2100))

    def test_raises_error_when_str_is_passed(self):
        with self.assertRaises(TypeError):
            is_leap("Sveiki")

    def test_None(self):
        self.assertIsNotNone("None")

        

