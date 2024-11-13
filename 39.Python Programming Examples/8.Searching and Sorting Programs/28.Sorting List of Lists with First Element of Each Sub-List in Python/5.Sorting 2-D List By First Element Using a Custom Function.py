# Using a Custom Function
def custom_sort(sub_list):
	return sub_list[0]

list_of_lists = [[3, 'b'], [1, 'a'], [2, 'c']]
sorted_list = sorted(list_of_lists, key=custom_sort)
#Display list in sorted order
print(sorted_list)
