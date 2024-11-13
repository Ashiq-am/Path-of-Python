# Python3 code to demonstrate working of
# Concatenate Rear elements in Tuple List
# Using join() + list comprehension

# initializing list
test_list = [(1, 2, "Gfg"), (4, "is"), ("Best", )]

# printing original list
print("The original list is : " + str(test_list))

# "-1" is used for access
res = " ".join([sub[-1] for sub in test_list])

# printing result
print("The Concatenated result : " + str(res))
