import unittest
from python_testing import is_prime

class Tests(unittest.TestCase):
    def test1(self):
        # Check that 1 is not prime
        self.assertFalse(is_prime(1))
    def test1(self):
        # Check that 2 is prime
        self.assertTrue(is_prime(2))
    def test1(self):
        # Check that 25 is not prime
        self.assertFalse(is_prime(25))
    
if __name__ == "__main__":
    unittest.main()