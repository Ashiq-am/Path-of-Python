# Python3 code to demonstrate working of
# Convert List to key-value list by prefic grouping
# Using groupby() + startswith() + lambda
from itertools import groupby

# initializing list
test_list = ["GFG-1", 4, 6, 7, "GFG-2", 2, 3, "GFG-3", 9, 2, 4, 6]

# printing original list
print("The original list : " + str(test_list))

# initializing prefix
temp = "GFG"

res = {}
# extracting result from grouped by prefix
for key, val in groupby(test_list, lambda ele: str(ele).startswith(temp)):

    # checking for existing key
    if key:
        k = next(val)
    else:
        res[k] = list(val)

# printing result
print("The constructed dictionary : " + str(res))
