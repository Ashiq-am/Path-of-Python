original_list = [1, 2, 3, 4, 2, 1, 5, 6, 4]
print("Original List:", original_list)

unique_list = []
[unique_list.append(x) for x in original_list if x not in unique_list]
print("Update List:", unique_list)
