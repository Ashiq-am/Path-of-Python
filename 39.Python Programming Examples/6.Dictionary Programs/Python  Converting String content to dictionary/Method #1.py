# Python3 code to demonstrate working of
# Converting String content to dictionary
# Using dictionary comprehension + split()

# initializing string
test_str = "Gfg = 1, Good = 2, CS = 3, Portal = 4"

# printing original string
print("The original string is : " + test_str)

# Using dictionary comprehension + split()
# Converting String content to dictionary
res = {key: int(val) for key, val in (item.split('=')
				for item in test_str.split(', '))}

# printing result
print("The newly created dictionary : " + str(res))
