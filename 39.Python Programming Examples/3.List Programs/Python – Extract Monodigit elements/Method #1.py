# Python3 code to demonstrate working of
# Extract Monodigit elements
# Using list comprehension + all()

# initializing list
test_list = [463, 888, 123, "aaa", 112, 111, "gfg", 939, 4, "ccc"]

# printing original lists
print("The original list is : " + str(test_list))

# all() checks for all similar digits
res = [sub for sub in test_list if all(
	str(ele) == str(sub)[0] for ele in str(sub))]

# printing result
print("Extracted Numbers : " + str(res))
