def sort_dict_using_loop(original_dict):
	sorted_dict = {}
	for key in sorted(original_dict, key=original_dict.get):
		sorted_dict[key] = original_dict[key]
	return sorted_dict


# Example Usage
original_dict = {'banana': 3, 'apple': 1, 'orange': 2}
print("Original Dictionary:", original_dict)

sorted_dict = sort_dict_using_loop(original_dict)
print("Sorted Dictionary ", sorted_dict)
