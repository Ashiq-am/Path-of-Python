import my_functions

def test_addition():
	result = my_functions.add_numbers(2, 3)
	assert result == 5, f"Expected 5, but got {result}"

def test_subtraction():
	result = my_functions.subtract_numbers(5, 2)
	assert result == 3, f"Expected 3, but got {result}"

def test_multiplication():
	result = my_functions.multiply_numbers(3, 4)
	assert result == 12, f"Expected 12, but got {result}"

def test_division():
	result = my_functions.divide_numbers(10, 2)
	assert result == 5, f"Expected 5, but got {result}"

	# Additional test for division by zero
	try:
		my_functions.divide_numbers(10, 0)
	except ValueError as e:
		assert str(e) == "Cannot divide by zero", f"Expected 'Cannot divide by zero', but got '{e}'"

def test_addition_negative():
	result = my_functions.add_numbers(-2, 3)
	assert result == 1, f"Expected 1, but got {result}"
