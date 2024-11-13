# Python program to fetch the indices
# of true values in a Boolean list
from itertools import compress

# initializing list
bool_list = [False, True, False, True, True, True]

# printing given list
print("Given list is : " + str(bool_list))

# using itertools.compress()
# to return true indices.
res = list(compress(range(len(bool_list)), bool_list))

# printing result
print("Indices having True values are : " + str(res))
