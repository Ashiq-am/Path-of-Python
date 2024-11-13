# Python code to replace every element
# in second list with index of first element.

# List initialization
Input1 = ['cut', 'god', 'pass']

# using enumeate
temp = {y:x for x, y in enumerate(Input1)}

# List initialization
Input2 = ['god', 'cut', 'cut', 'cut',
		'god', 'pass', 'cut', 'pass']

# Using list comprehension
Output = [temp.get(elem) for elem in Input2]

# Printing output
print("initial 2 list are")
print(Input1, "\n", Input2)
print("Second list after replacement is:", Output)
