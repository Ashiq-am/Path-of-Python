# test suite
import unittest

class TestStringMethods(unittest.TestCase):
	# test function to test whether key is present in container
	def test_positive(self):
		key = "gfgs"
		container = "geeksforgeeks"
		# error message in case if test case got failed
		message = "key is present in container."
		# assertNotIn() to check if key is in container
		self.assertNotIn(key, container, message)


if __name__ == '__main__':
	unittest.main()
