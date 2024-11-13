# import module
from itertools import chain

# initializing list
test_list = ["geeksforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing char range
strt, end = 14, 30

# strt and end used to get desired characters
res = ''.join(chain.from_iterable(test_list))[strt : end]

# printing result
print("Range characters : " + str(res))
