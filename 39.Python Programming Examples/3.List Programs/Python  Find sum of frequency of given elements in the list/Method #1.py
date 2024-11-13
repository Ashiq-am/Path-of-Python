# Python code to find sum of frequency of
# element of first list in second list.

# List initialization
Input1 = [1, 2, 3]
Input2 = [2, 1, 2, 1, 3, 5, 2, 3]

# Using sum
Output = sum(Input2.count(elem) for elem in Input1)

# Printing output
print("Initial list are:", Input1, Input2)
print("Frequency is:", Output)
