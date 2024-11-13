# test suite
import unittest


class TestStringMethods(unittest.TestCase):

    # negative test function to test if values1 is greater or equal than value2
    def test_negativeForGreaterEqual(self):
        first = 4
        second = 5

        # error message in case if test case got failed
        message = "first value is not greater or equal than second value."

        # assert function() to check if values1 is greater or equal than value2
        self.assertGreaterEqual(first, second, message)


if __name__ == '__main__':
    unittest.main()
