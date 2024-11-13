Input = [3, 4, 15, 6, 17, 8, 9]

# The index ranges to split at
Index_list = [(1, 3), (3, 6)]

result_list = []

for index_range in Index_list:
	result_list.append(Input[index_range[0]:index_range[1]+1])

print(result_list)
