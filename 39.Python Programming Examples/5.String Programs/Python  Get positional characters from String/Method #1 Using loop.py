# Python3 code to demonstrate working of
# Get positional characters from String
# using loop

# initializing string
test_str = "gfgisbest"

# printing original string
print("The original string is : " + test_str)

# initializing index list
indx_list = [1, 3, 4, 5, 7]

# Get positional characters from String
# using loop
res = ''
for ele in indx_list:
	res = res + test_str[ele]

# printing result
print("Substring of selective characters : " + res)
