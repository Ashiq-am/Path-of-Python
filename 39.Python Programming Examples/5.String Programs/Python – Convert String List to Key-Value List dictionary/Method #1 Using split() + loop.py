# Python3 code to demonstrate working of
# Convert String List to Key-Value List dictionary
# Using split() + loop

# initializing list
test_list = ["gfg is best for geeks", "I love gfg", "CS is best subject"]

# printing string
print("The original list : " + str(test_list))

res = dict()
for sub in test_list:
    # split() for key
    # packing value list
    key, *val = sub.split()
    res[key] = val

# printing results
print("The key values List dictionary : " + str(res))
