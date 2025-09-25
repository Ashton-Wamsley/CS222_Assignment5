import unittest
from CS222_Assignment5 import fahrenheitToCelsius, intToFibonacci

class TestAssignment5(unittest.TestCase):
    def testFahrenheitToCelsiusIfValid(self):
        self.assertAlmostEqual(fahrenheitToCelsius(32), 0.0)
        self.assertAlmostEqual(fahrenheitToCelsius(212), 100.0)
        self.assertAlmostEqual(fahrenheitToCelsius(98.6), 37.0, places = 1)
    
    def testFahrenheitToCelsiusIfInvalid(self):
        with self.assertRaises(TypeError):
            fahrenheitToCelsius("warm")
    
    def testFibBaseCases(self):
        self.assertEqual(intToFibonacci(0), 0)
        self.assertEqual(intToFibonacci(1), 1)
    
    def testFibGeneralCase(self):
        self.assertEqual(intToFibonacci(5), 5)
        self.assertEqual(intToFibonacci(10), 55)

    def testFibIfInvalidType(self):
        with self.assertRaises(TypeError):
            intToFibonacci(3.5)
    
    def testFibIfNegative(self):
        with self.assertRaises(ValueError):
            intToFibonacci(-1)
if __name__ == "__main__":
    unittest.main()