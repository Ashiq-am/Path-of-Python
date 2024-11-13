# test suite
import unittest


# test class
class Myclass:
    x = 5


class Myclass2:
    x = 5


class TestClass(unittest.TestCase):
    # test function to test whether obj is instance of class
    def test_negative(self):
        objectName = Myclass()
        # error message in case if test case got failed
        message = "given object is instance of Myclass."
        # assert function() to check if obj is instance of class
        self.assertNotIsInstance(objectName, Myclass2, message)


if __name__ == '__main__':
    unittest.main()
