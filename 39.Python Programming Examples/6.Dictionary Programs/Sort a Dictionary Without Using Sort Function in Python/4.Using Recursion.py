def sort_dict_recursive(original_dict):
	if not original_dict:
		return {}
	min_key = min(original_dict, key=original_dict.get)
	sorted_dict = {min_key: original_dict.pop(min_key)}
	sorted_dict.update(sort_dict_recursive(original_dict))
	return sorted_dict

# Example Usage
original_dict = {'banana': 3, 'apple': 1, 'orange': 2}
print("Original Dictionary:", original_dict)

sorted_dict = sort_dict_recursive(original_dict)
print("Sorted Dictionary :", sorted_dict)
