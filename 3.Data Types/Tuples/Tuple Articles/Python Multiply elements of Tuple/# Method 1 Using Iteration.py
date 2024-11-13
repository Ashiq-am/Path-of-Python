# Python code to convert list of tuple into list of elements
# formed by multiplying elements of tuple.

# Input list initialisation
Input = [(2, 3), (4, 5), (6, 7), (2, 8)]

# Output list initialisation
Output = []

# Iteration to multiply element and append multiplied element in
# new list
for elem in Input:
	temp = elem[0]*elem[1]
	Output.append(temp)

# printing output
print("The original list of tuple is ")
print(Input)

print("\nThe answer is")
print(Output)
