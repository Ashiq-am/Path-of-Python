# A Python program to print all
# permutations of given length
from itertools import permutations

# Get all permutations of length 2
# and length 2
perm = permutations([1, 2, 3], 2)

# Print the obtained permutations
for i in list(perm):
	print(i)






'''It generate nCr * r! permutations if length of input sequence is n and input parameter is r.'''