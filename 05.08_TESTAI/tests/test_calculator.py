import unittest
import calculator

class CalculatorTest(unittest.TestCase):
    def test_sudetis(self):
        self.assertEqual(calculator.sudetis(2,2),4)
        self.assertEqual(calculator.sudetis(-2,2),0)
        self.assertEqual(calculator.sudetis(5,2),7)
        self.assertEqual(calculator.sudetis(10,2),12)
        self.assertEqual(calculator.sudetis(100,2),102)

    def test_atimtis(self):
        self.assertEqual(5, calculator.atimtis(10, 5))
        self.assertEqual(-2, calculator.atimtis(-1, 1))
        self.assertEqual(0, calculator.atimtis(-1, -1))

    def test_daugyba(self):
        self.assertEqual(50, calculator.daugyba(10, 5))
        self.assertEqual(-1, calculator.daugyba(-1, 1))
        self.assertEqual(1, calculator.daugyba(-1, -1))

    def test_dalyba(self):
        self.assertEqual(2, calculator.dalyba(10, 5))
        self.assertEqual(-1, calculator.dalyba(-1, 1))
        self.assertEqual(1, calculator.dalyba(-1, -1))
        self.assertRaises(ZeroDivisionError, calculator.dalyba, 1,0)