import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(0, 1), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(5, 3), 2)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        with self.assertRaises(ValueError):
            divide(5, 0)
    # ##########################


    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)



    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()