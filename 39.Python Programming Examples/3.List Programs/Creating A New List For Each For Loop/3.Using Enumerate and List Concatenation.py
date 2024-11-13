# Example using enumerate and list concatenation
original_list = [1, 2, 3, 4, 5]
new_lists = []
for index, item in enumerate(original_list):
	new_lists.append([item * i for i in range(1, 4)])

# Output
print(new_lists)
