# Python3 code to demonstrate working of
# All numbers combinations
# Using loop + str() + int()
from itertools import combinations

# initializing list
test_list = [59, 236, 31, 38, 23]

# printing original list
print("The original list : " + str(test_list))

# All numbers combinations
# Using loop + str() + int()
res = []
for i in test_list:
    for j in test_list:
        if j != i:
            res.append(int(str(i) + str(j)))

# printing result
print("All numbers combinations : " + str(res))
