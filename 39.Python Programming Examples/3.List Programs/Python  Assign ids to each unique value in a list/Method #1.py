# Python3 code to demonstrate
# assigning ids to values
# using list comprehension + defaultdict + lambda
from collections import defaultdict

# initializing list
test_list = [5, 6, 7, 6, 5, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + defaultdict + lambda
# assigning ids to values
temp = defaultdict(lambda: len(temp))
res = [temp[ele] for ele in test_list]

# print result
print("The ids of assigned values is : " + str(res))
