#This is unit test module for prime_factors
#See http://content.codersdojo.org/code-kata-catalogue/prime-factors/
#For lanch test:
#$python test_prime_factors.py

import unittest
from prime_factors import get_prime_factors

class TestPrimeFactor(unittest.TestCase):
    """ Class for test get prime factor """
    def test_get_prime_factors(self):
        """
        Test get prime factors function
        """
        self.assertEqual(get_prime_factors(1), [])
        self.assertEqual(get_prime_factors(2), [2])
        self.assertEqual(get_prime_factors(3), [3])
        self.assertEqual(get_prime_factors(4), [2, 2])
        self.assertEqual(get_prime_factors(6), [2, 3])
        self.assertEqual(get_prime_factors(7), [7])
        self.assertEqual(get_prime_factors(8), [2, 2, 2])
        self.assertEqual(get_prime_factors(9), [3, 3])
        self.assertEqual(get_prime_factors(17), [17])
        self.assertEqual(get_prime_factors(353), [353])


if __name__ == '__main__':
    unittest.main()

