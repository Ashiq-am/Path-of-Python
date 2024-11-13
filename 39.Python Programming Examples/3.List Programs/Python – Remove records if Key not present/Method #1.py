# Python3 code to demonstrate working of
# Remove records if Key not present
# Using list comprehension

# initializing list
test_list = [{'Gfg': 1, 'Best': 3},
             {'Gfg': 3, 'Best': 5},
             {'Best': 3}]

# printing original list
print("The original list : " + str(test_list))

# initializing K Key
K = 'Gfg'

# Remove records if Key not present
# Using list comprehension
res = [ele for ele in test_list if K in ele]

# printing result
print("List after filteration : " + str(res))
