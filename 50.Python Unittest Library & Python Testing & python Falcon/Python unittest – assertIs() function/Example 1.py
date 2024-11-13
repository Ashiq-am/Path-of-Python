# unit test case
import unittest

class DummyClass:
    x = 5


class TestMethods(unittest.TestCase):

    # test function to test object equality of two value
    def test_negative(self):
        firstValue = DummyClass()
        secondValue = DummyClass()
        # error message in case if test case got failed
        message = "First value & second value are not evaluated to same object !"

        # assertIs() to check that if first & second evaluated to same object
        self.assertIs(firstValue, secondValue, message)

if __name__ == '__main__':
    unittest.main()
