# Python3 code to demonstrate
# Prefix frequency in List
# using sum() + startswith()

# Initializing list
test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

# printing original list
print("The original list is : " + str(test_list))

# Initializing substring
test_sub = 'gfg'

# Prefix frequency in List
# using sum() + startswith()
res = sum(sub.startswith(test_sub) for sub in test_list)

# printing result
print("Strings count with matching frequency : " + str(res))
