# Python3 program to insert
# an element into sorted list
import bisect

def insert(list, n):
	bisect.insort(list, n)
	return list

# Driver function
list = [1, 2, 4]
n = 3

print(insert(list, n))
