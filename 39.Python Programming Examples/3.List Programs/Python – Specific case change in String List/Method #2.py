# Python3 code to demonstrate
# Specific case change in String List
# using loop + capitalize()

# Initializing lists
test_list1 = ['GFG', 'IS', 'BEST', 'FOR', 'GEEKS']
test_list2 = ['Gfg', 'Best']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Specific case change in String List
# using loop + capitalize()
for idx, ele in enumerate(test_list1):
    if ele.capitalize() in test_list2:
        test_list1[idx] = ele.capitalize()

# printing result
print("The string list after case change is : " + str(test_list1))
