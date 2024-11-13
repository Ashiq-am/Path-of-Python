# Python code to convert list of tuple into list of elements
# formed by multiplying elements of tuple.

# Input list initialisation
Input = [(2, 3), (4, 5), (6, 7), (2, 8)]

# Iteration to multiply element and append multiplied element in
# new list
Output = [(x * y) for x, y in Input]

# printing output
print("The original list of tuple is ")
print(Input)

print("\nThe answer is")
print(Output)
