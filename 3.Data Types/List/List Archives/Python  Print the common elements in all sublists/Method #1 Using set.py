# Python code to find duplicate element in all
# sublist from list of list

# List of list initialization
Input = [ [10, 20, 30, 40],
		[30, 40, 60, 70],
		[20, 30, 40, 60, 70],
		[30, 40, 80, 90], ]

Output = set(Input[0])
for l in Input[1:]:
	Output &= set(l)

# Converting to list
Output = list(Output)

# Printing answer
print(Output)
