# Python code explaining
# SymPy.from_sequence()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.from_sequence() method

# creating vector
a = [2, 3, 1, 0]

# inverted vector of a
print ("vector a - from_sequence form : ",
	Permutation.from_sequence(a))

# length = 5, so permutation as per that.
print ("\nstring - from_sequence form : ",
	Permutation.from_sequence('GEEKS'))


# length = 5, so permutation as per that.
# defining a key
print ("\nstring - from_sequence form : ",
	Permutation.from_sequence('GEEKS', key = lambda x: x.lower()))
