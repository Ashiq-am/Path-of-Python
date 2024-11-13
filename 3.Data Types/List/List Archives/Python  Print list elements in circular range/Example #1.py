# Python code to print element in group
# of 5 till 9 iteration in circular range.

# Importing
from itertools import cycle

# list initialization
List = [90, 99, 192, 0, 43, 55]

# Defining no of iterations
n = 9

# Defining no of grouping
k = 5

for index, *ans in zip(range(n), *[cycle(List)] * k):
	# printing ans
	print(ans)
