# Python3 code to demonstrate working of
# Fractional Frequency of elements in List
# Using Counter() + loop + dictionary comprehension
from collections import Counter

# initializing list
test_list = [4, 5, 4, 6, 7, 5, 4, 5, 4, 6, 4, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing numerator
numer = {idx: 0 for idx in set(test_list)}

# initializing denominator
denom = Counter(test_list)

res = []
for ele in test_list:
    # increasing counter
    numer[ele] += 1
    res.append(str(numer[ele]) + '/' + str(denom[ele]))

# printing result
print("Fractional Frequency List : " + str(res))
