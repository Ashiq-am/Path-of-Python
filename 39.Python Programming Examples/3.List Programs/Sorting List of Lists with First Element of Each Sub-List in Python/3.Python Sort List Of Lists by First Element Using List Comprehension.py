# Using List Comprehension with Sorted
list_of_lists = [[3, 'b'], [1, 'a'], [2, 'c']]
sorted_list = [x for x in sorted(list_of_lists, key=lambda x: x[0])]

#Display sorted list
print(sorted_list)
