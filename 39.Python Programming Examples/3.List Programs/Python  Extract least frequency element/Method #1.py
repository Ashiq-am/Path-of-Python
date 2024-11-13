# Python3 code to demonstrate working of
# Extract least frequency element
# using defaultdict() + loop
from collections import defaultdict

# initialize list
test_list = [1, 3, 4, 5, 1, 3, 5]

# printing original list
print("The original list : " + str(test_list))

# Extract least frequency element
# using defaultdict() + loop
res = defaultdict(int)
for ele in test_list:

    res[ele] += 1
min_occ = 9999
for ele in res:
    if min_occ > res[ele]:
        min_occ = res[ele]
        tar_ele = ele

# printing result
print("The minimum occurring element is : " + str(tar_ele))
