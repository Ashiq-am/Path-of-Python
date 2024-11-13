# test suite
import unittest


class TestStringMethods(unittest.TestCase):

    # positive test function to test if values1 is greater than or equal to value2
    def test_positiveForGreaterEqual(self):
        first = 4
        second = 4

        # error message in case if test case got failed
        message = "first value is not greater or equal than second value."

        # assert function() to check if values1 is greater or equal than value2
        self.assertGreaterEqual(first, second, message)


if __name__ == '__main__':
    unittest.main()
