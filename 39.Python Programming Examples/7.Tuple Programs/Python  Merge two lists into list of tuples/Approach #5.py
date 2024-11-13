# Using map() and lambda
def listOfTuples(l1, l2):
	return list(map(lambda x, y:(x,y), l1, l2))

# Driver Code
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

print(listOfTuples(list1, list2))
