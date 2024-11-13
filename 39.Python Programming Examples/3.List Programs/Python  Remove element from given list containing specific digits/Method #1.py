# Python code to remove all those elements
# from list which contains certain digits

# Input List Initialisation
Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13, 15, 16]

# Numbers to delete
no_delete = [1, 0]

# Output List Initialisation
Output = []

# Using iteration to remove all the elements
for elem in Input:
	flag = 1
	temp = elem
	while elem > 0:
		rem = elem % 10
		elem = elem//10
		if rem in no_delete:
			flag = 0
	if flag == 1:
		Output.append(temp)

# Printing Output
print("Intial list is :", Input)
print("Delete list :", no_delete)
print("List after removing elements is :", Output)
