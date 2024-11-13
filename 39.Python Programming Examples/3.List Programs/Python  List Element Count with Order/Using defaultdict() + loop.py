# Python3 code to demonstrate working of
# List Element Count Order
# using defaultdict() + loop
from collections import defaultdict

# initialize list
test_list = [1, 4, 1, 5, 4, 1, 5]

# printing original list
print("The original list : " + str(test_list))

# List Element Count Order
# using defaultdict() + loop
temp = defaultdict(int)
res = []
for ele in test_list:
	temp[ele] += 1
	res.append((ele, temp[ele]))

# printing result
print("List elements with their order count : " + str(res))
