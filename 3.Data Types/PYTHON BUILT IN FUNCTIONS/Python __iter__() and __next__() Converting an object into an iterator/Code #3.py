# Python code demonstrating
# basic use of iter()

listB = ['Cat', 'Bat', 'Sat', 'Mat']


iter_listB = listB.__iter__()

try:
	print(iter_listB.__next__())
	print(iter_listB.__next__())
	print(iter_listB.__next__())
	print(iter_listB.__next__())
	print(iter_listB.__next__()) #StopIteration error
except:
	print(" \nThrowing 'StopIterationError'",
					"I cannot count more.")
