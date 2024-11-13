a = 34
b = "GeeksforGeeks"

try:
	# works normally
	print(float(a))

	# may lead to ValueError, so use try-except
	print(float(b))

except ValueError:
	print("Error: Unable to convert the string to a float.")
