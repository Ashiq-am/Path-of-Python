# Python3 code to demonstrate working of
# Key Columns Dictionary from Matrix
# Using zip() + dict()

# initializing lists
test_list1 = [[4, 6, 8], [8, 4, 2], [8, 6, 3]]
test_list2 = ["Gfg", "is", "Best"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# zip() used to map keys with values and return tuples
# as result
# * operator used to perform unpacking
res = dict(zip(test_list2, zip(*test_list1)))

# printing result
print("The paired dictionary : " + str(res))
