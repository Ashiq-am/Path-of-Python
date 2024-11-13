# Using a for-loop to create a list of lists
list_of_lists = []
rows = 3
columns = 3

for i in range(rows):
	inner_list = [j + 1 for j in range(columns)]
	list_of_lists.append(inner_list)

# Displaying the resulting list of lists
print(list_of_lists)
