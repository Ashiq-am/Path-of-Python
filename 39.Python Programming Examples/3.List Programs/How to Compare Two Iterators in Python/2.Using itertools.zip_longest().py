from itertools import zip_longest
def approach2Fn(iterator1, iterator2):
	return all(x == y for x, y in zip_longest(iterator1, iterator2))
# data
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 5]
iter1 = iter(list1)
iter2 = iter(list2)
print(approach2Fn(iter1, iter2))
