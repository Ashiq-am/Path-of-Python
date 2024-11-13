# Python3 code to demonstrate working of
# Extract Tuples with all Numeric Strings
# Using all() + list comprehension + isdigit()

# initializing list
test_list = [("45", "86"), ("Gfg", "1"), ("98", "10"), ("Gfg", "Best")]

# printing original list
print("The original list is : " + str(test_list))

# all() checks for all digits()
res = [sub for sub in test_list if all(ele.isdigit() for ele in sub)]

# printing result
print("Filtered Tuples : " + str(res))
