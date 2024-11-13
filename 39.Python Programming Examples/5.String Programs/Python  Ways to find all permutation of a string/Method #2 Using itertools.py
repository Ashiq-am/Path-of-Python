# Python code to demonstrate
# to find all permutation of
# a given string

from itertools import permutations

# Initialising string
ini_str = "abc"

# Printing initial string
print("Initial string", ini_str)

# Finding all permuatation
permutation = [''.join(p) for p in permutations(ini_str)]
# Printing result
print("Resultant List", str(permutation))
