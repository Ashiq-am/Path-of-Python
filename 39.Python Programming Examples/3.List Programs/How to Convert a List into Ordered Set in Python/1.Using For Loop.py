from collections import OrderedDict


def list_to_ordered_set(input_list):
	ordered_set = OrderedDict()
	for item in input_list:
		ordered_set[item] = None
	return set(ordered_set.keys())


# Example usage
input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result = list_to_ordered_set(input_list)
print(type(input_list))
print("Output:", result)
print(type(result))
