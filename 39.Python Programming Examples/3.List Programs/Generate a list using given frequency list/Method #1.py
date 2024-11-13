# Python code to generate list containing numbers from 0 to 'n'
# having frequency of no from another list

# List initialisation
Input = [1, 4, 3, 5]
Output = []

# Number initialisation
no = 0

# using iteration
for rep in Input:
	for elem in range(rep):
		Output.append(no)
	no += 1

# printing output
print(Output)
