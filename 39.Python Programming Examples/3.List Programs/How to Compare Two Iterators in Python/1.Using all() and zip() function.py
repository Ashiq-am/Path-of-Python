def approach1Fn(iterator1, iterator2):
	return all(x == y for x, y in zip(iterator1, iterator2))

# data
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
iter1 = iter(list1)
iter2 = iter(list2)
print(approach1Fn(iter1, iter2))
