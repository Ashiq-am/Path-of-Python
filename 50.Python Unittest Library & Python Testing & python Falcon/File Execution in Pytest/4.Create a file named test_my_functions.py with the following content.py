from my_functions import add_numbers

def test_addition():
	result = add_numbers(2, 3)
	# This assertion will fail
	assert result == 6
