# Python code to find common first
# element in list of tuple

# Importing
from collections import defaultdict

# Function to solve the task
def find(pairs):
	mapp = defaultdict(list)
	for x, y in pairs:
		mapp[x].append(y)
	return [(x, *y) for x, y in mapp.items()]

# Input list initialization
Input = [('p', 'q'), ('p', 'r'),
		('p', 's'), ('m', 't')]

# calling function
Output = find(Input)

# Printing
print("Initial list of tuple is :", Input)
print("List showing common first element", Output)
