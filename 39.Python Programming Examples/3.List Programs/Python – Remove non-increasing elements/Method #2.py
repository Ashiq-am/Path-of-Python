# Python3 code to demonstrate working of
# Remove non-increasing elements
# Using list comprehension + max + zip() + accumulate
from itertools import accumulate

# initializing list
test_list = [5, 3, 4, 5, 7, 3, 9, 10, 3, 10, 12, 13, 3, 16, 1]

# printing original list
print("The original list is : " + str(test_list))

# checking for each element with curr maximum computed using zip
res = [idx for idx, ele in zip(test_list, accumulate(test_list, max)) if idx == ele]

# printing result
print("The list after removing non-increasing elements : " + str(res))
