# test suite
import unittest

class TestStringMethods(unittest.TestCase):
	# test function to test whether key is present in container
	def test_negative(self):
		key = "gfg"
		container = "geeksforgeeks"
		# error message in case if test case got failed
		message = "key is not in container."
		# assertIn() to check if key is in container
		self.assertIn(key, container, message)

if __name__ == '__main__':
	unittest.main()
