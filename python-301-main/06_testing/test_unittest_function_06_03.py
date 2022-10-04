import unittest
import unittest_function_06_03 as unf


class TestUnittestFunction(unittest.TestCase):

    def test_double(self):
        num = unf.double_or_nothing(4)
        self.assertGreater(num, 0)

    def test_nothing(self):
        num = unf.double_or_nothing(5)
        self.assertEqual(num, 0)


if __name__ == "__main__":
    unittest.main()
