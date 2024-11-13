# Python code to sort list of tuple based on sum of element in tuple.

# Input list initialisation
Input = [(4, 5), (2, 3), (6, 7), (2, 8)]

print("The original list of tuple is ")
print(Input)

# Passing lambda as key to sort list of tuple
Input.sort(key = lambda x: x[0] + x[1])

# Printing output
print("\nThe answer is")
print(Input)
