# Python code to demonstrate
# how to join pair of elements of list

# Initialising list
ini_list = iter(['a', 'b', 'c', 'd', 'e', 'f'])

# Pairing the elements of lists
res = [h + next(ini_list, '') for h in ini_list]

# Printing final result
print ("Result", str(res))
