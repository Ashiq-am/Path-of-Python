# Python3 code to demonstrate working of
# Element frequencies in percent range
# Using Counter() + set() + loop + len()
from collections import Counter

# initializing list
test_list = [4, 6, 2, 4, 6, 7, 8, 4, 9, 1, 4, 6, 7, 8]

# printing original list
print("The original list is : " + str(test_list))

# initializing percent ranges
strt, end = 13, 25

# getting frequencies
freqs = dict(Counter(test_list))

# computing percents and assiging
res = []
for ele in set(test_list):
	percent = (freqs[ele] / len(test_list)) * 100
	if percent >= strt and percent <= end:
		res.append(ele)

# printing result
print("Elements within range of frequencies : " + str(res))
