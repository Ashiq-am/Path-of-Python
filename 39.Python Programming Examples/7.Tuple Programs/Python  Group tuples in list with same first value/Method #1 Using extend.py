# Python code to find common
# first element in list of tuple

# Function to solve the task
def find(Input):
	out = {}
	for elem in Input:
		try:
			out[elem[0]].extend(elem[1:])
		except KeyError:
			out[elem[0]] = list(elem)
	return [tuple(values) for values in out.values()]

# List initialization
Input = [('x', 'y'), ('x', 'z'), ('w', 't')]

# Calling function
Output = (find(Input))

# Printing
print("Initial list of tuple is :", Input)
print("List showing common first element", Output)
