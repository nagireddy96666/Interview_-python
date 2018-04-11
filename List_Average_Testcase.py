from List_Average import add
import unittest
class Test(unittest.TestCase):
    def setup(self):
        pass
    def test_list(self):
        self.assertEqual(add(),5)
if __name__ == '__main__':
    unittest.main()

