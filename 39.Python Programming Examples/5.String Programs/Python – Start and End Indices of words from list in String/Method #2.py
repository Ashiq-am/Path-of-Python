# Python3 code to demonstrate working of
# Start and End Indices of words from list in String
# Using dictionary comprehension + len() + index()

# initializing string
test_str = "gfg is best for all CS geeks and engineering job seekers"

# printing original string
print("The original string is : " + str(test_str))

# initializing check_list
check_list = ["geeks", "engineering", "best", "gfg"]

# Dictionary comprehension to be used as shorthand for
# forming result Dictionary
res = {key: [test_str.index(key), test_str.index(key) + len(key) - 1]
	for key in check_list if key in test_str}

# printing result
print("Required extracted indices : " + str(res))
