# Python3 program to reshape a list
# according to multidimensional list

def reshape(lst1, lst2):
	iterator = iter(lst2)
	return [[next(iterator) for _ in sublist]
						for sublist in lst1]

# Driver code
list1 = [[1], [2, 3], [4, 5, 6]]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(reshape(list1, list2))
