original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
condition = lambda x: x % 2 == 0 # Example condition: remove even numbers

# Creating a copy of the list to avoid modifying it during iteration
for x in original_list[:]:
	if condition(x):
		original_list.remove(x)

print(original_list)
