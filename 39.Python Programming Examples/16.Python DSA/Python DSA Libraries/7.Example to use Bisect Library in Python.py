import bisect

# Sorted list
sorted_list = [1, 3, 5, 7, 9]

# Element to insert
new_element = 6

# Find the insertion point using bisect_left
insertion_point = bisect.bisect_left(sorted_list, new_element)

# Insert the element into the sorted list
sorted_list.insert(insertion_point, new_element)

print("Sorted list after insertion:", sorted_list)
print("New element inserted at index:", insertion_point)
