# Python3 code to demonstrate working of
# Group Sum till each K
# Using loop
from collections import defaultdict

# initializing list
test_list = [2, 3, 5, 6, 2, 6, 8, 9, 4, 6, 1]

# printing original lists
print("The original list is : " + str(test_list))

# initializing K
K = 6

temp_sum = 0
res = []
for ele in test_list:
	if ele != K:
		temp_sum += ele

	# append and re initializing if K occurs
	else:
		res.append(temp_sum)
		res.append(ele)
		temp_sum = 0

res.append(temp_sum)

# printing result
print("Computed list : " + str(res))
