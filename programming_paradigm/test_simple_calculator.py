import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test the perfomance of simple calculator class."""
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
         self.assertEqual(self.calc.add(1, 5), 6)
         self.assertEqual(self.calc.add(10, 10),20)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertIsNone(self.calc.divide(10, 0))
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)

        
    