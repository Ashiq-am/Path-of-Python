# Python3 code to demonstrate working of
# Summation of consecutive elements power
# Using defaultdict() + loop + sum()
from collections import defaultdict

# initializing list
test_list = [2, 2, 2, 3, 3, 3, 3, 4, 4, 5]

# printing original lists
print("The original list is : " + str(test_list))

# getting frequency
temp = defaultdict(int)
for ele in test_list:
	temp[ele] += 1

temp = dict(temp)

# computing summation
res = sum([key ** temp[key] for key in temp])

# printing result
print("Computed summation of powers : " + str(res))
