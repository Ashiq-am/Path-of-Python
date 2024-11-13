def is_float_digit_replace(value):
	# Handling the case for one decimal point
	cleaned_value = value.replace(".", "", 1)

	# Check if the cleaned string consists only of digits
	return cleaned_value.isdigit()

input_string = "123.45"
result = is_float_digit_replace(input_string)
print(f"String: {input_string}\nCan be converted to float: {result}")
