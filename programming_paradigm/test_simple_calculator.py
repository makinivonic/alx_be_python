import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test the perfomance of simple calculator class."""

    def test_calculator(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(1, 5), 6)
        self.assertEqual(calc.add(10, 10),20)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertIsNone(calc.divide(10, 0))
        self.assertEqual(calc.multiply(10, 5), 50)

    