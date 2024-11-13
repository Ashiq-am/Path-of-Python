# Python code to demonstrate working
# of binary search in library
from bisect import bisect_right

def BinarySearch(a, x):
	i = bisect_right(a, x)
	if i != len(a)+1 and a[i-1] == x:
		return (i-1)
	else:
		return -1

a = [1, 2, 4, 4]
x = int(4)
res = BinarySearch(a, x)
if res == -1:
	print(x, "is absent")
else:
	print("Last occurrence of", x, "is present at", res)
