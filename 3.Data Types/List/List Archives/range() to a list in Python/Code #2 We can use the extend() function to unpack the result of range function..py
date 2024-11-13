# Create an empty list
My_list = []

# Value to begin and end with
start, end = 10, 20

# Check if start value is smaller than end value
if start < end:
	# unpack the result
	My_list.extend(range(start, end))
	# Append the last value
	My_list.append(end)

# Print the list
print(My_list)
