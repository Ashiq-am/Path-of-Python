# Python3 code to demonstrate working of
# Alternate List elements
# Using zip() + loop

# initializing lists
test_list1 = [5, 3, 1, 4, 7]
test_list2 = [6, 4, 2, 5, 1]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Using zip() to perform pairing and loop to
# get elements into result list
res = []
for ele1, ele2 in zip(test_list1, test_list2):
    res.append(ele1)
    res.append(ele2)

# printing result
print("The zig-zag printing of elements : " + str(res))
