# Python3 code to demonstrate working of
# Construct dictionary using random values
# Using randint() + loop
from random import randint

# initializing list
test_list = ["Gfg", "is", "Best"]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 9

# assiging random elements
# dictionary comprehension used as shorthand
res = {ele : randint(i, j) for ele in test_list}

# printing result
print("Random range initialized dictionary : " + str(res))
