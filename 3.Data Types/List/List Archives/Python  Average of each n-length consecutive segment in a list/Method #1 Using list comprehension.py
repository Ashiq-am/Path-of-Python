# Python code to find average of each consecutive segment

# List initialisation
Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
		12, 13, 14, 15, 16, 17, 18, 19, 20]

# Defining Splits
splits = 5

# Finding average of each consecutive segment
Output = [sum(Input[i:i + splits])/splits
		for i in range(len(Input) - splits + 1)]

# printing output
print(Output)
