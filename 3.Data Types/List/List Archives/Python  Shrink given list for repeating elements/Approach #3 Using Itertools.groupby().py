# Python3 program to Shrink list
# for repeating elements
from itertools import groupby

def shrinkList(lst):
	return ([(element, len(list(i)))
	for element, i in groupby(lst)])

# Driver Code
lst = [1, 1, 1, 2, 2, 3, 3, 4]
print(shrinkList(lst))
