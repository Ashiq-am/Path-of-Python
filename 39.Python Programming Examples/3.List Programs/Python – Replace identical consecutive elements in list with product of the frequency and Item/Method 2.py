# Python3 code to demonstrate working of
# Equal Consecution Product
# Using groupby() + sum()
from itertools import groupby

# initializing list
test_list = [3, 3, 3, 3, 6, 7, 5, 5, 5, 8, 8, 6, 6, 6, 6, 6, 1, 1, 1, 2, 2]

# printing original list
print("The original list is : " + str(test_list))

# creating Consecution groups and summing for required values
res = [sum(grup) for k, grup in groupby(test_list)]

# printing result
print("Elements after equal Consecution product : " + str(res))
