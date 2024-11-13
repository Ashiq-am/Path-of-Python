# Python code to find frequency of a character
# at every position of list in list of lists.

# Input list initialization
Input = [['X', 'Y', 'X'], ['Z', 'Y', 'X'],
		['Y', 'Y', 'Y'], ['Z', 'Z', 'X'],
		['Y', 'Z', 'X']]
Output = []

# Character Initialization
character = 'X'

# Output list initialization
for elem in range(len(Input[0])):
	Output.append(0)

# Using iteration
for elem in Input:
	for x, y in enumerate(elem):
		if y == character:
			Output[x]+= 1
for x, y in enumerate(Output):
	Output[x] = y / len(Input)

# Printing
print("Initial list of list is :", Input)
print("Occurrence of 'X' in list is", Output)
