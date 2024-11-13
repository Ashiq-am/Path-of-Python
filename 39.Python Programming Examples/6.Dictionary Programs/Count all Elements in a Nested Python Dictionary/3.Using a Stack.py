def count_elements_stack(nested_dict):
	count = 0
	stack = [nested_dict]

	while stack:
		current_dict = stack.pop()
		for value in current_dict.values():
			if isinstance(value, dict):
				stack.append(value)
			else:
				count += 1

	return count

# Example
nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
total_elements = count_elements_stack(nested_dict)
print(f"Total elements in the nested dictionary: {total_elements}")
