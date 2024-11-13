# Python3 code to demonstrate working of
# Filter uppercase characters Tuples
# Using list comprehension + all() + isupper()

# initializing list
test_list = [("GFG", "IS", "BEST"), ("GFg", "AVERAGE"), ("GFG", ), ("Gfg", "CS")]

# printing original list
print("The original list is : " + str(test_list))

# all() returns true only when all strings are uppercase
res = [sub for sub in test_list if all(ele.isupper() for ele in sub)]

# printing results
print("Filtered Tuples : " + str(res))
