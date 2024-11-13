# Python3 code to demonstrate working of
# Restrict Elements Frequency in List
# Using loop + defaultdict()
from collections import defaultdict

# initializing list
test_list = [1, 4, 5, 4, 1, 4, 4, 5, 5, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing restrct_dict
restrct_dict = {4: 3, 1: 1, 6: 1, 5: 2}

res = []
lookp = defaultdict(int)
for ele in test_list:
    lookp[ele] += 1

    # move to next ele if greater than restrct_dict count
    if lookp[ele] > restrct_dict[ele]:
        continue
    else:
        res.append(ele)

# printing results
print("Filtered List : " + str(res))
