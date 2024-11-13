lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

merged_list = []
for sublist in lists:
	merged_list.extend(sublist)

print("The Merged list is")
print(merged_list)
