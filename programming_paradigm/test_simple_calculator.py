# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
    

import unittest
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3,5), 8)
        self.assertEqual(self.calc.add(3,-3), 0)
        self.assertEqual(self.calc.add(3,-5), -2)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(90, 10), 80)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(-25, -10), -15)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(9, 5), 45)
        self.assertEqual(self.calc.multiply(2, 15), 30)
        self.assertEqual(self.calc.multiply(0, 0), 0)


    def test_divide(self):
        self.assertEqual(self.calc.divide(2,1), 2)
        self.assertEqual(self.calc.divide(3,0), None)
        self.assertEqual(self.calc.divide(-84,2), -42)

    
if __name__ == "__main__":
    unittest.main()  