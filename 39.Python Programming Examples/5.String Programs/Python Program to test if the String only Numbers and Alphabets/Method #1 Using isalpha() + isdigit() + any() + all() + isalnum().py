# Python3 code to demonstrate working of
# Test if string contains both Numbers and Alphabets only
# Using isalpha() + isdigit() + any() + all() + isalnum()

# initializing string
test_str = 'Geeks4Geeks'

# printing original string
print("The original string is : " + str(test_str))

# conditional combination for getting result.
res = not ((all(idx.isdigit() for idx in test_str) or (all(idx.isalpha()
			for idx in test_str)) or (any(not idx.isalnum() for idx in test_str))))

# printing result
print("Does string contain both numbers and alphabets only? : " + str(res))
