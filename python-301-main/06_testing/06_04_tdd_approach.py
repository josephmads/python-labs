# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest

class TestStringsUp(unittest.TestCase):

# 1) A function that takes a string and capitalizes it.
    def test_string_up(self):
        str_up = string_up("hi everybody")
        self.assertEqual(str_up, "HI EVERYBODY")

#  2) A function that takes a string and repeats it twice and adds spaces in between.
    def test_string_repeat(self):
        str_rpt = string_repeat("hello")
        self.assertEqual(str_rpt, "hello hello hello")
