# Python code to demonstrate
# how to join pair of elements of list

# Initialising list
ini_list = ['a', 'b', 'c', 'd', 'e', 'f']

# Printing initial list
print ("Initial list", str(ini_list))

# Pairing the elements of lists
res = [i + j for i, j in zip(ini_list[::2], ini_list[1::2])]

# Printing final result
print ("Result", str(res))
