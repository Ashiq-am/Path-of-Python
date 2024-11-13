# A Python program to print all combinations
# of given length with duplicates in input
from itertools import combinations

# Get all combinations of [1, 1, 3]
# and length 2
comb = combinations([1, 1, 3], 2)

# Print the obtained combinations
for i in list(comb):
	print(i)
