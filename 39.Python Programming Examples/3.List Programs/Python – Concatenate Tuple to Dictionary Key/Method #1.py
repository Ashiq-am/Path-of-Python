# Python3 code to demonstrate working of
# Concatenate Tuple to Dictionary Key
# Using loop + join()

# initializing list
test_list = [(("gfg", "is", "best"), 10), (("gfg", "good"), 1), (("gfg", "for", "cs"), 15)]

# printing original list
print("The original list is : " + str(test_list))

res = {}
for sub in test_list:
    # joining for making key
    res[" ".join(sub[0])] = sub[1]

# printing result
print("The computed Dictionary : " + str(res))
