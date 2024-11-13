# Python code to replace every element
# in second list with index of first element.

# List initialization
Input1 = ['cut', 'god', 'pass']

# List initialization
Input2 = ['god', 'cut', 'cut', 'cut',
		'god', 'pass', 'cut', 'pass']

elem = {k: i for i, k in enumerate(Input1)}
Output = list(map(elem.get, Input2))

# Printing output
print("initial 2 list are")
print(Input1, "\n", Input2)
print("Second list after replacement is:", Output)
