# Python3 code to demonstrate
# Group elements from Dual List Matrix
# using loop + list comprehension

# Initializing lists
test_list1 = ['Gfg', 'is', 'best']
test_list2 = [['Gfg', 1], ['is', 2], ['best', 1], ['Gfg', 4], ['is', 8], ['Gfg', 7]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Group elements from Dual List Matrix
# using loop + list comprehension
res = {key: [] for key in test_list1}
for key in res:
    res[key] = [sub[1] for sub in test_list2 if key == sub[0]]

# printing result
print("The dictionary after grouping : " + str(res))
