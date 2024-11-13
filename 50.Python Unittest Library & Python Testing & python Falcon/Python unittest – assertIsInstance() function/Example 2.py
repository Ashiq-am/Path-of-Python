# test suite
import unittest

# test class
class Myclass:
	x = 5


class TestClass(unittest.TestCase):
	# test function to test whether obj is instance of class
	def test_positive(self):
		objectName = Myclass()
		# error message in case if test case got failed
		message = "given object is not instance of Myclass."
		# assertIsInstance() to check if obj is instance of class
		self.assertIsInstance(objectName, Myclass, message)


if __name__ == '__main__':
	unittest.main()
