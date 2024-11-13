from itertools import zip_longest

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for item1, item2 in zip_longest(list1, list2, fillvalue=None):
    print(item1, item2)
