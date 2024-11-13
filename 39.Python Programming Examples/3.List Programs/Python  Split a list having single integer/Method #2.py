# Python code to split list containing single integer

# List initialization
input = [231]

# Using list comprehension
output = [int(x) if x.isdigit() else x
		for z in input for x in str(z)]

# Printing output
print(output)
