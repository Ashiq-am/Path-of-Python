# Python3 code to demonstrate working of
# Custom elements repetition
# Using loop + zip()

# initializing lists
test_list1 = ["Gfg", "is", "Best"]
test_list2 = [4, 3, 5]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using zip() to intervene elements and occurrence
res = []
for ele, occ in zip(test_list1, test_list2):
    res.extend([ele] * occ)

# printing result
print("The repeated list : " + str(res))
