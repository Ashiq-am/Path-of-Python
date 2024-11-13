# Python3 code to demonstrate working of
# Concatenate Strings in Order
# Using loop

# initializing list
test_list = ["best", "Gfg", "for", "is", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing join order
sort_order = [1, 3, 0, 2, 4]

res = ''
for ordr in sort_order:
    # concatenating by order
    res += test_list[ordr]

# printing result
print("Ordered concatenation : " + str(res))
