# Python code to remove all duplicates
# and permutations in nested list

#Initialisation
input = [[-11, 0, 11], [-11, 11, 0], [-11, 2, -11],
					[-11, -11, 2], [2, -11, -11]]

# Sorting tuple then removing
output = set(tuple(sorted(x)) for x in input)

# printing output
print(output)
