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

res = dict()
for ele in test_list:
    # assiging random elements
    res[ele] = randint(i, j)

# printing result
print("Random range initialized dictionary : " + str(res))
