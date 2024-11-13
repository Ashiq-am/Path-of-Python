# Python3 code to demonstrate
# removing consecutive duplicates
# using groupby() + list comprehension
from itertools import groupby

# initializing list
test_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using groupby() + list comprehension
# removing consecutive duplicates
res = [i[0] for i in groupby(test_list)]

# printing result
print ("The list after removing consecutive duplicates : " + str(res))
