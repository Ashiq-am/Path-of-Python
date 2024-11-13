# Python code to find frequency of a character
# at every position of list in list of lists.

# Input list initialization
Input = [['X', 'Y', 'X'], ['Z', 'Y', 'X'],
		['Y', 'Y', 'Y'], ['Z', 'Z', 'X'],
		['Y', 'Z', 'X']]

Output = []

# Character initialization
character = 'X'

# Using zip
Output = [elem.count(character)/len(elem)
				for elem in zip(*Input)]

# Printing
print("Initial list of list is :", Input)
print("Occurrence of 'X' in list is", Output)
