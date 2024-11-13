from unittest.mock import patch
import example
@patch('example.func')

def test1(x, mock_func):
	# Uses patched example.func
	example.func(x)
	mock_func.assert_called_with(x)
