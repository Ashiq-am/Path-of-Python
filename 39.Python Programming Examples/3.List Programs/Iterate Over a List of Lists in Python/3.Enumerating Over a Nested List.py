nested_list = [[1, 2, 3], [4, 5], [7, 8]]

for i, inner_list in enumerate(nested_list):
	for j, element in enumerate(inner_list):
		print(f"Value at index ({i}, {j}): {element}")
