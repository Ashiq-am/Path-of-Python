# A Stack based Python3 program to find next
# smaller element for all array elements
# in same order as input.using System;

""" prints element and NSE pair for all
elements of arr[] of size n """


def printNSE(arr, n):
	s = []
	mp = {}

	# push the first element to stack
	s.append(arr[0])

	# iterate for rest of the elements
	for i in range(1, n):
		if (len(s) == 0):
			s.append(arr[i])
			continue

		""" if stack is not empty, then
		pop an element from stack.
		If the popped element is greater
		than next, then
		a) print the pair
		b) keep popping while elements are
		greater and stack is not empty """
		while (len(s) != 0 and s[-1] > arr[i]):
			mp[s[-1]] = arr[i]
			s.pop()

		""" push next to stack so that we can find
		next smaller for it """
		s.append(arr[i])

	""" After iterating over the loop, the remaining
	elements in stack do not have the next smaller
	element, so print -1 for them """
	while (len(s) != 0):
		mp[s[-1]] = -1
		s.pop()

	for i in range(n):
		print(arr[i], "--->", mp[arr[i]])


arr = [11, 13, 21, 3]
n = len(arr)
printNSE(arr, n)
