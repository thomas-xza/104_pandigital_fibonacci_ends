#!/usr/bin/env python3

import unittest

# gen_next_fibonacci()

# - hardcoded expected fibonacci values, based on initial easily-verified sequence

# convert_f_n_to_set()

# - any number (including non-fibonacci) of length 9+ checks functionality
# - number of length below 9 doesn't need to throw exception

# check_f_n()

# - f_n set length too small
# - f_n set length correct, 0 sets are pandigital
# - f_n set length correct, 1 set is pandigital
# - f_n set length correct, 2 sets are pandigital


# check_set()

# - set of expected length for which true is expected
# - set of expected length for which false is expected


##  Simplest possible import, not suitable in scaled contexts.

from fib_funcs import *


class Test_104(unittest.TestCase):


    def test_gen_next_fibonacci(self):

        self.assertEqual(gen_next_fibonacci((1, 1)), (1, 2))
        self.assertEqual(gen_next_fibonacci((1, 2)), (2, 3))
        self.assertEqual(gen_next_fibonacci((2, 3)), (3, 5))


    def test_convert_f_n_to_set(self):

        self.assertEqual(len(convert_f_n_to_sets(12345678987654321)[0]), 9)
        self.assertEqual(len(convert_f_n_to_sets(12345678987654321)[1]), 9)
    

if __name__ == '__main__':
    unittest.main()
