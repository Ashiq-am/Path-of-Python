# Python3 program to Sort tuple based
# on occurrence of first element
from collections import OrderedDict

def sortOnOccurence(lst):
	dct = {}
	for i, j in lst:
		dct.setdefault(i, []).append(j)
	return([(k, ) + tuple(OrderedDict.fromkeys(v)) + (len(v), )
	for k, v in dct.items()])

# Driver code
lst = [(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]
print(sortOnOccurence(lst))
