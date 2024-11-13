# Python3 code to demonstrate working of
# Get positional characters from String
# using generator expression + enumerate()

# initializing string
test_str = "gfgisbest"

# printing original string
print("The original string is : " + test_str)

# initializing index list
indx_list = [1, 3, 4, 5, 7]

# Get positional characters from String
# using generator expression + enumerate()
res = ''.join((char for idx, char in enumerate(test_str) if idx in indx_list))

# printing result
print("Substring of selective characters : " + res)
