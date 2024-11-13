# Python program to copy a nested list

# List initialization
Input_list = [[0, 1, 2], [3, 4, 5], ]
Output = []

# Using iteration to assign values
for x in range(len(Input_list)):
	temp = []
	for elem in Input_list[x]:
		temp.append(elem)
	Output.append(temp)

# Printing Output
print("Initial list is:")
print(Input_list)
print("New assigned list is")
print(Output)
