# Python3 code to Update a list
# of tuples according to another list

def merge(list1, list2):
	dic = dict(list1)
	dic.update(dict(list2))
	return list(dic.items())

# Driver Code
list1 = [('a', 0), ('b', 0), ('c', 0)]
list2 = [('a', 5), ('c', 3)]
print(merge(list1, list2))
