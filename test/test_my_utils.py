import unittest
import sys
import random
import numpy as np

sys.path.append('src')  # noqa
sys.path.append('test')  # noqa

import my_utils


class TestMyUtils(unittest.TestCase):
    def test_get_column(self):
        print("Testing mssg")
        # test return type
        self.assertIsInstance(my_utils.get_column(
            'Agrofood_co2_emission.csv', 0, 'Zimbabwe', result_column=1), list)

    # calc_mean tests
    def test_calc_mean_fixed(self):
        self.assertAlmostEqual(my_utils.calc_mean([1, 2, 3]), 2)
        self.assertAlmostEqual(my_utils.calc_mean([1.1, 2.2, 3.3]), 2.2)

    def test_calc_mean_error(self):
        self.assertRaises(ArithmeticError, my_utils.calc_mean, [])

    def test_calc_mean_random(self):
        # random cases
        for i in range(1, 1000):
            # generate arbitrary list length up to 1000 elements
            arr = [random.randint(0, 1000000)
                   for _ in range(random.randint(1, 1000))]

            # a mean is strictly less than the sum of all the elements
            self.assertTrue(my_utils.calc_mean(arr) <= sum(arr))

            # a mean is strictly geq the smallest element
            self.assertTrue(my_utils.calc_mean(arr) >= min(arr))

            # a mean is strictly leq the smallest element
            self.assertTrue(my_utils.calc_mean(arr) <= max(arr))

    # calc_median tests
    def test_calc_median_fixed(self):
        self.assertEqual(my_utils.calc_median([1, 2, 3]), 2)
        self.assertEqual(my_utils.calc_median([1.1, 2.2, 3.3]), 2.2)

    def test_calc_median_error(self):
        self.assertRaises(ArithmeticError, my_utils.calc_median, [])

    def test_calc_median_random(self):
        # random cases
        for i in range(1, 1000):
            # generate arbitrary list length up to 1000 elements
            arr = [random.randint(0, 1000000)
                   for _ in range(random.randint(1, 1000))]

            # a median is strictly less than the sum of all the elements
            self.assertTrue(my_utils.calc_median(arr) <= sum(arr))

            # a median is strictly geq the smallest element
            self.assertTrue(my_utils.calc_median(arr) >= min(arr))

            # a median is strictly leq the smallest element
            self.assertTrue(my_utils.calc_median(arr) <= max(arr))

    # calc_stdev tests
    def test_calc_stdev_fixed(self):
        self.assertAlmostEqual(my_utils.calc_stdev([1, 2, 3]) ** 2, 2/3)
        self.assertAlmostEqual(my_utils.calc_stdev([1.1, 2.2, 3.3]) ** 2,
                               2 * (1.1 ** 2) / 3)

    def test_calc_stdev_error(self):
        self.assertRaises(ArithmeticError, my_utils.calc_stdev, [])
        self.assertRaises(ArithmeticError, my_utils.calc_stdev, [1])

    def test_calc_stdev_random(self):
        # random cases
        for i in range(1, 1000):
            # generate arbitrary list length up to 1000 elements
            arr = [random.randint(0, 1000000)
                   for _ in range(random.randint(2, 1000))]

            # a standard deviation is positive (and nonzero if not all elements
            # are the same)
            if len(set(arr)) == 1:
                self.assertTrue(my_utils.calc_stdev(arr) == 0)
            else:
                self.assertTrue(my_utils.calc_stdev(arr) > 0)


if __name__ == "__main__":
    unittest.main()
