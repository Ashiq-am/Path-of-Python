with patch('example.func') as mock_func:
	example.func(x)
	mock_func.assert_called_with(x)
