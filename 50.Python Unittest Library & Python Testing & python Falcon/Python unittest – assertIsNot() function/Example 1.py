# unit test case
import unittest

class DummyClass:
    x = 5

class TestMethods(unittest.TestCase):
	# test function
	def test_negative(self):
		firstValue = DummyClass()
		secondValue = firstValue
		# error message in case if test case got failed
		message = "First value & second value evaluates to same object !"
		# assertIs() to check that if first & second don't evaluated to same object
		self.assertIsNot(firstValue, secondValue, message)

if __name__ == '__main__':
	unittest.main()
