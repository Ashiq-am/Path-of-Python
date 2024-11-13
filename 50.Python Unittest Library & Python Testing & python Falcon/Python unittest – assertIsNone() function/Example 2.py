# unit test case
import unittest

class DummyClass:
    x = 5

class TestMethods(unittest.TestCase):
	# test function
	def test_positive(self):
		firstValue = None
		# error message in case if test case got failed
		message = "Test value is not none."
		# assertIsNone() to check that if input value is none
		self.assertIsNone(firstValue, message)

if __name__ == '__main__':
	unittest.main()
