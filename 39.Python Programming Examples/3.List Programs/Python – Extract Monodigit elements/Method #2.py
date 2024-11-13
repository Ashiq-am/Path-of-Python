# Python3 code to demonstrate working of
# Extract Monodigit elements
# Using filter() + lambda + all()

# initializing list
test_list = [463, 888, 123, "aaa", 112, 111, "gfg", 939, 4, "ccc"]

# printing original lists
print("The original list is : " + str(test_list))

# all() checks for all similar digits
# filter() used for filtering
res = list(filter(lambda sub: all(str(ele) == str(
	sub)[0] for ele in str(sub)), test_list))

# printing result
print("Extracted Numbers : " + str(res))
