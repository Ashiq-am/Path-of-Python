# Python3 code to demonstrate working of
# Minimum elements for String construction
# Using issubset() + set() + combinations()
from itertools import combinations

# initializing list
test_list = ["geek", "ring", "sfor", "ok", "woke"]

# printing original list
print("The original list is : " + str(test_list))

# initializing target string
tar_str = "working"

res = -1
set_str = set(tar_str)
done = False
for val in range(0, len(test_list) + 1):

    # creating combinations
    for sub in combinations(test_list, val):

        # contructing sets of each combinations
        temp_set = set(ele for subl in sub for ele in subl)

        # checking if target string has created set as subset
        if set_str.issubset(temp_set):
            res = val
            done = True
            break
    if done:
        break

# printing result
print("The Minimum count elements for string : " + str(res))
