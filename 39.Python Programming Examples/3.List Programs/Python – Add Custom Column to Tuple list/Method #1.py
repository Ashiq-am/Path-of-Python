# Python3 code to demonstrate working of
# Add Custom Column to Tuple list
# Using list comprehension + zip()

# initializing list
test_list = [(3, 4), (78, 76), (2, 3)]

# printing original list
print("The original list is : " + str(test_list))

# initializing add list
cus_eles = [17, 23, 12]

# Add Custom Column to Tuple list
# Using list comprehension + zip()
res = [sub + (val, ) for sub, val in zip(test_list, cus_eles)]

# printing result
print("The tuples after adding elements : " + str(res))
