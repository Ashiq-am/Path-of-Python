import operator
def approach4Fn(iterator1, iterator2):
	return all(map(operator.eq, iterator1, iterator2))
# data
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 5]
iter1 = iter(list1)
iter2 = iter(list2)

print(approach4Fn(iter1, iter2))
