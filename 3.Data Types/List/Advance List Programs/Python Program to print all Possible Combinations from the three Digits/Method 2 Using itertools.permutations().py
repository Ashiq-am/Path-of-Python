# Python program to print all
# the possible combinations

from itertools import permutations

# Get all combination of [1, 2, 3]
# of length 3
comb = permutations([1, 2, 3], 3)

for i in comb:
	print(i)
