from itertools import chain

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
a = ['True', 'False', 'True']
combined_list = list(chain(list1, list2,a))

print(combined_list)
