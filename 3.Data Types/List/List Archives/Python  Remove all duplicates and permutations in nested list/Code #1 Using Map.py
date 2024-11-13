# Python code to remove all duplicates
# and permutations in nested list

#Initialisation
listOfPermut = [[-11, 0, 11], [-11, 11, 0], [-11, 0, 11],
				[-11, 2, -11], [-11, -11, 2], [2, -11, -11]]

# Sorting tuple then removing
output = set(map(lambda x: tuple(sorted(x)),listOfPermut))

# printing output
print(output)
