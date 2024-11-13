# test suite
import unittest


class TestStringMethods(unittest.TestCase):

    # positive test function to test if
    # values are almost equal with place
    def test_positiveForLess(self):
        first = 2
        second = 3

        # error message in case if test case got failed
        message = "first value is not less that second value."

        # assert function() to check if values1 is
        # less than value2
        self.assertLess(first, second, message)


# main for function call
if __name__ == '__main__':
    unittest.main()
