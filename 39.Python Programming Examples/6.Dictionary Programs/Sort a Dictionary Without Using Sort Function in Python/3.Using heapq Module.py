import heapq

def sort_dict_heapq(original_dict):
	sorted_items = heapq.nsmallest(len(original_dict),
								original_dict.items(), key=lambda x: x[1])

	sorted_dict = dict(sorted_items)
	return sorted_dict

# Example Usage
original_dict = {'banana': 3, 'apple': 1, 'orange': 2}
print("Original Dictionary:", original_dict)

sorted_dict = sort_dict_heapq(original_dict)
print("Sorted Dictionary:", sorted_dict)
