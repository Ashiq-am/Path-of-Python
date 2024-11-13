# unit test case
import unittest

class TestMethods(unittest.TestCase):
	# test function
	def test_negative(self):
		firstValue = None
		# error message in case if test case got failed
		message = "Test value is none."
		# assertIsNotNone() to check that if input value is not none
		self.assertIsNotNone(firstValue, message)

if __name__ == '__main__':
	unittest.main()
