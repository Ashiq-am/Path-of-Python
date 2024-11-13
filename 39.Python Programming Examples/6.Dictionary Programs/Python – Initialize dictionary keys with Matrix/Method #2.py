# Python3 code to demonstrate working of
# Initialize dictionary keys with Matrix
# Using deepcopy()
from copy import deepcopy

# initializing N
num = 4

# Initialize dictionary keys with Matrix
# Using deepcopy()
temp = [[] for idx in range(num)]
res = {'gfg': deepcopy(temp), 'best': deepcopy(temp)}

# printing result
print("The Initialized dictionary : " + str(res))
