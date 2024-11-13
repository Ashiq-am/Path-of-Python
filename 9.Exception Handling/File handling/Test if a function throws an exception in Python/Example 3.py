import unittest

class MyTestCase(unittest.TestCase):

    # Returns true if 100 / 0 raises an Exception
    def test_1(self):
        with self.assertRaises(ZeroDivisionError):
            100 / 0

if __name__ == '__main__':
    unittest.main()
