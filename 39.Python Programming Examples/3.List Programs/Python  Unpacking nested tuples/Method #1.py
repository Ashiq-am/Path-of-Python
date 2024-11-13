# Python3 code to demonstrate working of
# Unpacking nested tuples
# using list comprehension

# initialize list
test_list = [(4, (5, 'Gfg')), (7, (8, 6))]

# printing original list
print("The original list is : " + str(test_list))

# Unpacking nested tuples
# using list comprehension
res = [(x, y, z) for x, (y, z) in test_list]

# printing result
print("The unpacked nested tuple list is : " + str(res))
