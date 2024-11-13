# Python3 code to demonstrate
# removing consecutive duplicates
# using zip_longest()+ list comprehension
from itertools import zip_longest

# initializing list
test_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using zip_longest()+ list comprehension
# removing consecutive duplicates
res = [i for i, j in zip_longest(test_list, test_list[1:])
												if i != j]

# printing result
print ("List after removing consecutive duplicates : " + str(res))
