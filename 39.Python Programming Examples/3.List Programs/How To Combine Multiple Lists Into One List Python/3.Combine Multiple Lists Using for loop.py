lists = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
organized_list = []

for inner_list in lists:
	organized_list.extend(inner_list)

print(organized_list)
