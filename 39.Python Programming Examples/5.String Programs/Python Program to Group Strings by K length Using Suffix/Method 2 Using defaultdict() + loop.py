# Python3 code to demonstrate working of
# Group Strings by K length Suffix
# Using defaultdict() + loop
from collections import defaultdict

# initializing list
test_list = ["food", "peak", "geek",
             "good", "weak", "sneek"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

res = defaultdict(list)
for ele in test_list:
    # extracting suffix
    suff = ele[-K:]

    # appending into matched suffix key
    res[suff].append(ele)

# printing result
print("The grouped suffix Strings : " + str(dict(res)))
