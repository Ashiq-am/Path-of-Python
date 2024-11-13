# Python3 code to demonstrate
# Double each consecutive duplicate
# using loop + defaultdict()
from collections import defaultdict

# Initializing list
test_list = [1, 2, 4, 2, 4, 1, 2]

# printing original list
print("The original list is : " + str(test_list))

# Double each consecutive duplicate
# using loop + defaultdict()
temp = defaultdict(int)
res = []
for ele in test_list:
    temp[ele] += ele
    res.append(temp[ele])

# printing result
print("The list after manipulation is : " + str(res))
