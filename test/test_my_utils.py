import unittest
import sys

sys.path.append('./src') # noqa
sys.path.append('./test')

import my_utils


class TestMyUtils(unittest.TestCase):
    # all test functions have to be prefixed "test_"
    def test_add(self):
        # want to minimize the number of asserts used here, because the actual reporting of test pass/fail is at the function level, it's harder to access which assert is failing 
        # at maximum, test only one function, with positive tests, negative tests, and potential failures (e.g div by zero), like shown below. wouldn't want to test a subtract() function here, for example
        self.assertEqual(math_lib.add(5,10),15)
        self.assertEqual(math_lib.add(5,-10),-5)