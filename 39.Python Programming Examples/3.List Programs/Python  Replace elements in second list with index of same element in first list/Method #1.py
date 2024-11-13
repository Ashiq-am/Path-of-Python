# Python code to replace every element
# in second list with index of first element.

# List Initialization
Input1 = ['cut', 'god', 'pass']
Input2 = ['god', 'cut', 'cut', 'cut',
		'god', 'pass', 'cut', 'pass']

# List Initialization
Output = []

# Using iteration
for x in Input2:
	for y in Input1:
		if x == y:
			Output.append(Input1.index(y))

# Printing output
print("initial 2 list are")
print(Input1, "\n", Input2)
print("Second list after replacement is:", Output)
