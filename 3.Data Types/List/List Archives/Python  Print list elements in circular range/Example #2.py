# Python code to print element in group
# of 6 till 4 iteration in circular range.

# Importing
from itertools import cycle

# list initialization
List = ['Geeks', 'for', 'geeks', 'is', 'portal']

# Defining no of iterations
n = 4

# Defining no of grouping
k = 6

for index, *ans in zip(range(n), *[cycle(List)] * k):
	# printing ans
	print(ans)
