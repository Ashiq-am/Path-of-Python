# Python3 code to demonstrate working of
# Concatenate Dynamic Frequency
# Using defaultdict() + "+" operator + str()
from collections import defaultdict

# initializing list
test_list = ['z', 'z', 'e', 'f', 'f', 'e', 'f', 'z', 'c']

# printing original list
print("The original list is : " + str(test_list))

memo = defaultdict(int)
res = []
for ele in test_list:
    memo[ele] += 1

    # adding Frequency with element
    res.append(str(memo[ele]) + str(ele))

# printing result
print("Dynamic Frequency list : " + str(res))
