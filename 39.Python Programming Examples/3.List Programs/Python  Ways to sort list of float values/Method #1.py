# Python code to sort list of decimal values

# List initialization
Input = [12.8, .178, 1.8, 782.7, 99.8, 8.7]

# Using sorted and lambda
Output = sorted(Input, key = lambda x:float(x))

# Printing output
print(Output)
