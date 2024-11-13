# Python3 code to demonstrate working of
# Custom elements repetition
# Using loop + extend()

# initializing lists
test_list1 = ["Gfg", "is", "Best"]
test_list2 = [4, 3, 5]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using loop to perform iteration
res = []
for idx in range(0, len(test_list1)):
    # using extend to perform element repetition
    res.extend([test_list1[idx]] * test_list2[idx])

# printing result
print("The repeated list : " + str(res))
