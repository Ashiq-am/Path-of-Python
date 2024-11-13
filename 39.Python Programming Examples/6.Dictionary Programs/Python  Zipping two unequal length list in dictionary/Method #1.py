# Python code to demonstrate
# return the sum of values of a dictionary
# with same keys in the list of dictionary

from itertools import cycle

# Initialising list of dictionary
ini_lis1 = ['a', 'b', 'c', 'd', 'e']
ini_lis2 = [1, 2, 3]

# zipping in cyclic if shorter length
result = dict(zip(ini_lis1, cycle(ini_lis2)))

# printing resultant dictionary
print("resultant dictionary : ", str(result))
