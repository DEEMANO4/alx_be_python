import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -2), -7)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, -5), -5)
        self.assertEqual(self.calc.add(4, -1), 3)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3)
        # Add more assertions to thoroughly test the add method.


    def test_subtracion(self):
        "test_subtraction" "test_subtraction(self)"
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, -5), 5)
        self.assertEqual(self.calc.subtract(4, -1), 5)
        self.assertEqual(self.calc.subtract(2.5, 3.5), 1)
        self.assertEqual(self.calc.subtract(0.1, 0.2), -0.1)


    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -2), 10)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(0, -5), 0)
        self.assertEqual(self.calc.multiply(4, -1), -4)
        self.assertEqual(self.calc.multiply(2.5, 3.5), 8.75)
        self.assertEqual(self.calc.multiply(0.1, 0.2), 0.02)


    def test_division(self):
        """Test the division method"""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(2, 3), 0.66)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-5, -2), 2.5)
        self.assertEqual(self.calc.divide(7, 0), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)
        self.assertEqual(self.calc.divide(4, -1), -4)
        self.assertEqual(self.calc.divide(2.5, 3.5), 0.71)
        self.assertEqual(self.calc.divide(0.1, 0.2), 0.5)

        
# Remember to write additional test methods for subtract, multiply, and divide.