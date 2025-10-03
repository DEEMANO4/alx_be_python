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


    #def test_subtracion(self):
    #    """Test the subtraction method."""
        
# Remember to write additional test methods for subtract, multiply, and divide.