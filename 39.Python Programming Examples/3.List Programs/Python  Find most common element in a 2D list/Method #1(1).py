# Python3 program to find most
# common element in a 2D list
from itertools import chain

def mostCommon(lst):
	flatList = list(chain.from_iterable(lst))
	return max(flatList, key=flatList.count)

# Driver code
lst = [[10, 20, 30], [20, 50, 10], [30, 50, 10]]
print(mostCommon(lst))
