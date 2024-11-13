import unittest

class MyTestCase(unittest.TestCase):

    # Returns true if 1 + '1' raises a TypeError
    def test_1(self):
        with self.assertRaises(Exception):
            1 + '1'


if __name__ == '__main__':
    unittest.main()
