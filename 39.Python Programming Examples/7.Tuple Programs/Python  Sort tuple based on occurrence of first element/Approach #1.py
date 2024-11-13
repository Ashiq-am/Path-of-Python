# Python3 program to Sort tuple based
# on occurrence of first element
def sortOnOccurence(lst):
	dct = {}
	for i, j in lst:
		dct.setdefault(i, []).append(j)
	return([(i, *dict.fromkeys(j), len(j))
				for i, j in dct.items()])

# Driver code
lst = [(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]
print(sortOnOccurence(lst))
