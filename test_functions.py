"""
Program: test_functions.py
Author: Cara Krug
Last date modified: 09/06/2020

Program specifications: The program will have will prompt for the age of one infant (age 1-5 years) who is attending camp
and convert the age in months to years via a function call then print the result.
"""
import unittest
from main import camper_age_input


class MyTestCase(unittest.TestCase):

    def test_convert_to_months(self):
        self.assertEquals(camper_age_input.convert_to_months(28), 336.0)

    def test_convert_to_months_low(self):
        self.assertEquals(camper_age_input.convert_to_months(4), 48)

    def test_convert_to_months_high(self):
        self.assertEquals(camper_age_input.convert_to_months(72), 864)


if __name__ == '__main__':
    unittest.main()
