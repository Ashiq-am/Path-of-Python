# Python3 code to demonstrate working of
# Key Columns Dictionary from Matrix
# Using list comprehension + dictionary comprehension

# initializing lists
test_list1 = [[4, 6, 8], [8, 4, 2], [8, 6, 3]]
test_list2 = ["Gfg", "is", "Best"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using enumerate to get column numbers
# dictionary comprehension to compile result
res = {key: [sub[idx] for sub in test_list1] for idx, key in enumerate(test_list2)}

# printing result
print("The paired dictionary : " + str(res))
