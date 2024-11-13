# import our applictaion file
import my_app

# import library
import unittest

class FlaskTestCase(unittest.TestCase):

	def setUp(self):
		my_app.app.testing = True
		self.app = my_app.app.test_client()

	def test_home(self):
		result = self.app.get('/')
