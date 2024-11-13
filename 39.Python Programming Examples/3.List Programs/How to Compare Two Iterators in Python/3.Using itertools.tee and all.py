from itertools import tee

def compare_iterators(iterator1, iterator2):
	iter1_copy, iter2_copy = tee(iterator1), tee(iterator2)
	return all(x == y for x, y in zip(iter1_copy, iter2_copy))

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 5]
iter1 = iter(list1)
iter2 = iter(list2)

print(compare_iterators(iter1, iter2))
