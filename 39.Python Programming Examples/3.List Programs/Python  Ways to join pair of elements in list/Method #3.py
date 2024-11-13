# Python code to demonstrate
# how to join pair of elements of list

# Initialising list
ini_list = ['a', 'b', 'c', 'd', 'e', 'f']

# Printing initial lists
print ("Initial list", str(ini_list))

# Pairing the elements of lists
res = [ini_list[i] + ini_list[i + 1]
	for i in range(0, len(ini_list), 2)]

# Printing final result
print ("Result", str(res))
