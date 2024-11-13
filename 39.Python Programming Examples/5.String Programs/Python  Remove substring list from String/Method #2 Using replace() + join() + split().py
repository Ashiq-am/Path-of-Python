# Python3 code to demonstrate working of
# Remove substring list from String
# Using replace() + join() + split()

# initializing string
test_str = "gfg is best for all geeks"

# printing original string
print("The original string is : " + test_str)

# initializing sub list
sub_list = ["best", "all"]

# Remove substring list from String
# Using replace() + join() + split()
for sub in sub_list:
	test_str = test_str.replace(sub, ' ')
res = " ".join(test_str.split())

# printing result
print("The string after substring removal : " + res)
