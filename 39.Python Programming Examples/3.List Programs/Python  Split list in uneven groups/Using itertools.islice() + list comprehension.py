# Python3 code to demonstrate working of
# Split list in uneven groups
# using itertools.islice() + list comprehension
from itertools import islice

# initialize list
test_list = [1, 4, 5, 7, 6, 5, 4, 2, 10]

# initialize split list
split_list = [3, 4, 2]

# printing original list
print("The original list is : " + str(test_list))

# printing split list
print("The split list is : " + str(split_list))

# Split list in uneven groups
# using itertools.islice() + list comprehension
temp = iter(test_list)
res = [list(islice(temp, 0, ele)) for ele in split_list]

# printing result
print("The resultant split list is : " + str(res))
