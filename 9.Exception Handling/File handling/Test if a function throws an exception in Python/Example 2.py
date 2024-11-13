import unittest

class MyTestCase(unittest.TestCase):

    # Returns false if 1 + 1 raises no Exception
    def test_1(self):
        with self.assertRaises(Exception):
            1 + 1

if __name__ == '__main__':
    unittest.main()
