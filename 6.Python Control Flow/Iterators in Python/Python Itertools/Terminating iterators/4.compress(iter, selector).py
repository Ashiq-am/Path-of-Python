# Python code to demonstrate the working of
# and compress()


import itertools


# using compress() selectively print data values
print ("The compressed values in string are : ", end ="")
print (list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))
