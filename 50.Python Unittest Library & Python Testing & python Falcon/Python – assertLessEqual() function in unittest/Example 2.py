# test suite
import unittest


class TestStringMethods(unittest.TestCase):

    # positive test function to test if value1 is less or equal than value2
    def test_positiveForLessEqual(self):
        first = 4
        second = 4

        # error message in case if test case got failed
        message = "first value is not less than or equal to second value."

        # assert function() to check if values1 is less or equal than value2
        self.assertLessEqual(first, second, message)


if __name__ == '__main__':
    unittest.main()
