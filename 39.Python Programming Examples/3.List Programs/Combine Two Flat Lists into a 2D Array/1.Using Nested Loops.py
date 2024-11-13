list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result_array = []
for item1 in list1:
	inner_array = []
	for item2 in list2:
		inner_array.append([item1, item2])
	result_array.extend(inner_array)

print(result_array)
