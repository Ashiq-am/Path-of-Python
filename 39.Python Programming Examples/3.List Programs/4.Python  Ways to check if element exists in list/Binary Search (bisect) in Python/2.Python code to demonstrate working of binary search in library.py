# Python code to demonstrate working
# of binary search in library
from bisect import bisect_left

def BinarySearch(a, x):
	i = bisect_left(a, x)
	if i:
		return (i-1)
	else:
		return -1

# Driver code
a = [1, 2, 4, 4, 8]
x = int(7)
res = BinarySearch(a, x)
if res == -1:
	print("No value smaller than ", x)
else:
	print("Largest value smaller than ", x, " is at index ", res)
