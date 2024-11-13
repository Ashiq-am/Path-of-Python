# Python code to demonstrate
# to find common prefix
# from set of strings

from itertools import takewhile

# Initialising string
ini_strlist = ['akshat', 'akash', 'akshay', 'akshita']

# Finding commom prefix using Naive Approach
res = ''.join(c[0] for c in takewhile(lambda x:
		all(x[0] == y for y in x), zip(*ini_strlist)))

# Printing result
print("Resultant prefix", str(res))
