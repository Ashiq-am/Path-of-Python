# Python3 code to demonstrate working of
# Consecutive Tuple difference
# Using tuple() + map() + sub
from operator import sub

# initializing lists
test_list = [(6, 3), (1, 4), (8, 5), (3, 5)]

# printing original list
print("The original list : " + str(test_list))

# using loop to iterate elements
# using sub and map() to perform the subtraction to whole elements
res = []
for idx in range(len(test_list) - 1):
    res.append(tuple(map(sub, test_list[idx + 1][0:], test_list[idx][0:])))

# printing result
print("The extracted list : " + str(res))
