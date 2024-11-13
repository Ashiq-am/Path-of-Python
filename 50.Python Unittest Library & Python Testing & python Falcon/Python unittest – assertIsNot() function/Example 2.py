# unit test case
import unittest

class DummyClass:
    x = 5

class TestMethods(unittest.TestCase):
	# test function to test object equality of two value
	def test_positive(self):
		firstValue = DummyClass()
		secondValue = DummyClass()
		# error message in case if test case got failed
		message = "First value and second value evaluated to same object !"
		# assertIs() to check that if first & second don't evaluates to same object
		self.assertIsNot(firstValue, secondValue, message)

if __name__ == '__main__':
	unittest.main()
