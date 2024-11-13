# Python code to split string in substring manner

# Input initialisation
Input = "Geeks_for_geeks_is_best"

# Split initialise
split_string = Input.split('_')

# Output list initialise
Output = []

# Iteration
for a in range(len(split_string)):
	temp = split_string[:a + 1]
	temp = "_".join(temp)
	Output.append(temp)

# print output
print(Output)
