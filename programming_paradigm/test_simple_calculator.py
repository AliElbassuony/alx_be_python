import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class."""
    
    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the add method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed positive and negative
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        # Test with floats
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
    
    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test mixed positive and negative
        self.assertEqual(self.calc.subtract(1, -1), 2)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Test with floats
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
    
    def test_multiplication(self):
        """Test the multiply method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        # Test mixed positive and negative
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test with floats
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)
    
    def test_division(self):
        """Test the divide method with various inputs."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test division resulting in float
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        # Test division by 1
        self.assertEqual(self.calc.divide(7, 1), 7)
        # Test division of negative numbers
        self.assertEqual(self.calc.divide(-4, -2), 2)
        # Test division with floats
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=7)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()