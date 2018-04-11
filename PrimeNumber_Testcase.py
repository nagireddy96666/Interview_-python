from Given_Number_Prime_Or_Not import prime
import unittest
class Test(unittest.TestCase):
    def setup(self):
        pass
    def test_prime(self):
        self.assertTrue(prime(7),True)
if __name__ == '__main__':
    unittest.main()
