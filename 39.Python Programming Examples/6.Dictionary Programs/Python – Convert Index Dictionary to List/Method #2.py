# Python3 code to demonstrate working of
# Convert Index Dictionary to List
# Using list comprehension + get()

# initializing dictionary
test_dict = { 2 : 'Gfg', 4 : 'is', 6 : 'Best' }

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Index Dictionary to List
# Using list comprehension + get()
res = [test_dict.get(ele, 0) for ele in range(10)]

# printing result
print("The converted list : " + str(res))
