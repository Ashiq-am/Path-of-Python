import unittest
from unittest.mock import patch
def get_user_input():
    user_input = input("Enter something: ")
    return user_input
class TestUserInput(unittest.TestCase):
    @patch('builtins.input', return_value='test_input')
    def test_get_user_input(self, mock_input):
        self.assertEqual(get_user_input(), 'test_input')
if __name__ == '__main__':
    unittest.main()
