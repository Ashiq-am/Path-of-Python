numerator = 10
denominator = 0

try:
	result = numerator / denominator
except ZeroDivisionError:
	print("Error: Cannot divide by zero.")