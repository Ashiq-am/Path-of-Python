# Python3 code to demonstrate working of
# Subtract String Lists
# using loop + remove()

# initialize lists
test_list1 = ["gfg", "is", "best", "for", "CS"]
test_list2 = ["preffered", "is", "gfg"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Subtract String Lists
# using loop + remove()
res = [ ele for ele in test_list1 ]
for a in test_list2:

    if a in test_list1:
        res.remove(a)

# printing result
print("The Subtracted list is : " + str(res))
