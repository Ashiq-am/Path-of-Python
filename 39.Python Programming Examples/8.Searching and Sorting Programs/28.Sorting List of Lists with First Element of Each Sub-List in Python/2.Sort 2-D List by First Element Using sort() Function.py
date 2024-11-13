#Using the sort() Method with a Custom Comparator
list_of_lists = [[3, 'b'], [1, 'a'], [2, 'c']]
list_of_lists.sort(key=lambda x: x[0])

#Display the sorted list
print(list_of_lists)
