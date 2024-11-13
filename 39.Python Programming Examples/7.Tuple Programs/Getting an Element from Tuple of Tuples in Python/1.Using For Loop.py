# Example tuple of tuples
tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Accessing an element using a for loop
target_element = None
for inner_tuple in tuple_of_tuples:
	for element in inner_tuple:
		if element == 6:
			target_element = element
			break

print("Using a for loop:", target_element)
