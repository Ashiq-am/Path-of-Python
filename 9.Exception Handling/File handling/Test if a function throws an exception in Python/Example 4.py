import unittest

class MyTestCase(unittest.TestCase):

# Returns true if GeeksforGeeks.txt file is not present and raises an EnvironmentError
# Exception
# In this example expected exception is RuntimeError while generated exception is
# EnvironmentError, thus returns false
	def test_1(self):
		with self.assertRaises(RuntimeError):
			file = open("GeeksforGeeks.txt", 'r')

if __name__ == '__main__':
	unittest.main()
