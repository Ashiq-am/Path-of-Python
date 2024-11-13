# Python code to demonstrate
# return the sum of values of dictionary
# with same keys in list of dictionary

from itertools import cycle

# Initialising list of dictionary
ini_lis1 = ['a', 'b', 'c', 'd', 'e']
ini_lis2 = [1, 2, 3]

# zipping in cyclic if shorter length
result = {v: ini_lis2[i % len(ini_lis2)]
		for i, v in enumerate(ini_lis1)}

print("resultant dictionary : ", str(result))
