# Python3 code to demonstrate
# Remove characters till K element
# using list comprehension + enumerate() + index()

# Initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 'best'

# Remove characters till K element
# using list comprehension + enumerate() + index()
temp = test_list.index(K)
res = [ele for idx, ele in enumerate(test_list) if idx > temp]

# printing result
print ("List elements after removing all before K : " + str(res))
