# initialize a list
my_list = [1, 2, 3, 1, 5, 4]
indices = [ind for ind, ele in enumerate(my_list) if ele == 1]

# print the indices
print(indices)
