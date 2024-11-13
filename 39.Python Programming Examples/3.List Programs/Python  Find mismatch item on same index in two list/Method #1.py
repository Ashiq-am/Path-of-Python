# Python code to find the index at which the
# element of two list doesn't match.

# List initialisation
Input1 = [1, 2, 3, 4]
Input2 = [1, 5, 3, 6]

# Index initialisation
y = 0

# Output list intialisation
Output = []

# Using iteration to find
for x in Input1:
	if x != Input2[y]:
		Output.append(y)
	y = y + 1

# Printing output
print(Output)
