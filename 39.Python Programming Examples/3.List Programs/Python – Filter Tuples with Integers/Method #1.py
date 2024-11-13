# Python3 code to demonstrate working of
# Filter Tuples with Integers
# Using loop + isinstance()

# initializing list
test_list = [(4, 5, "GFg"), (5, 6), (3,), ("Gfg",)]

# printing original list
print("The original list is : " + str(test_list))

res_list = []
for sub in test_list:
    res = True
    for ele in sub:

        # checking for non-int.
        if not isinstance(ele, int):
            res = False
            break
    if res:
        res_list.append(sub)

# printing results
print("Filtered tuples : " + str(res_list))
