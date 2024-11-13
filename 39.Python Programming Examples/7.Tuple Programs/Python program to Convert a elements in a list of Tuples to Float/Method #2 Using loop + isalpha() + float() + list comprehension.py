# Python3 code to demonstrate working of
# Convert Tuple List elements to Float
# Using loop + isalpha() + float

# initializing list
test_list = [("3", "Gfg"), ("1", "26.45"), ("7.32", "8"), ("Gfg", "8")]

# printing original list
print("The original list is : " + str(test_list))

res = []
for tup in test_list:
    # list comprehension to check for each case
    temp = [ele if ele.isalpha() else float(ele) for ele in tup]
    res.append((temp[0], temp[1]))

# printing result
print("The converted list : " + str(res))
