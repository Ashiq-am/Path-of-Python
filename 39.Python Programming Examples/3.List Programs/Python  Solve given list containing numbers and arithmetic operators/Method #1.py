# Python code to solve the list
# containing numbers and arithmetic operators

# Importing
from operator import add, sub

# Function to solve list
def find(Input):
	ans = 0
	options = {'+': add, '-': sub}
	option = add
	for item in Input:
		if item in options:
			option = options[item]
		else:
			number = float(item)
			ans = option(ans, number)
	return ans

# Input Initialization
lst = [91, '+', 132, '-', 156, '+', 4]

# Calling function
Output = find(lst)

# Printing output
print("Initial list", lst)
print("Answer after solving list is:", Output)
