# Python3 code to demonstrate working of
# Extract odd length words in String
# Using list comprehension

# initializing string
test_str = "gfg is best of geeks"

# printing original string
print("The original string is : " + test_str)

# Extract odd length words in String
# Using list comprehension
res = [ele for ele in test_str.split() if len(ele) % 2]

# printing result
print("The odd length strings are : " + str(res))
