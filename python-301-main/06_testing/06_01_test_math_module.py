# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)
    
    def test_pow_returns_x_to_power_y(self):
        self.assertEqual(math.pow(2,3), 8)

if __name__ == "__main__":
    unittest.main()