# Python3 code to demonstrate
# Specific case change in String List
# using loop + upper() + enumerate()

# Initializing lists
test_list1 = ['GFG', 'IS', 'BEST', 'FOR', 'GEEKS']
test_list2 = ['Gfg', 'Best']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Specific case change in String List
# using loop + upper() + enumerate()
for idx, ele in enumerate(test_list1):
    for ele2 in test_list2:
        if ele == ele2.upper():
            test_list1[idx] = ele2

# printing result
print("The string list after case change is : " + str(test_list1))
