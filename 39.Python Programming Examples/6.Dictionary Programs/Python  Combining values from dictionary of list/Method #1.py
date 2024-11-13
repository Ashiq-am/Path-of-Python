# Python code to combine every key value
# pair in every combinations

# List initialization
Input = {
"Bool" : ["True", "False"],
"Data" : ["Int", "Float", "Long Long"],
}

# Importing
import itertools as it

# Sorting input
sorted_Input = sorted(Input)

# Using product after sorting
Output = [dict(zip(sorted_Input, prod))
		for prod in it.product(*(Input[sorted_Input]
		for sorted_Input in sorted_Input))]

# Printing output
print(Output)
