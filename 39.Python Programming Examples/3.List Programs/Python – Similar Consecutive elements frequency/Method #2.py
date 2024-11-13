# Python3 code to demonstrate
# Similar Consecutive elements frequency
# using groupby() + len() + list comprehension
from itertools import groupby

# initializing list
test_list = [2, 2, 3, 3, 3, 3, 4, 4, 4]

# printing original list
print ("The original list is : " + str(test_list))

# Similar Consecutive elements frequency
# using groupby() + len() + list comprehension
res = [(k, len(list(j))) for k, j in groupby(test_list)]

# printing result
print ("The consecutive element frequency is : " + str(res))
