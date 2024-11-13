# Python3 code to demonstrate working of
# Case Counter in String
# using map() + sum() + isupper + islower

# initializing string
test_str = "GFG is For GeeKs"

# printing original string
print("The original string is : " + test_str)

# Case Counter in String
# using map() + sum() + isupper + islower
res_upper = sum(map(str.isupper, test_str))
res_lower = sum(map(str.islower, test_str))

# printing result
print("The count of Upper case characters : " + str(res_upper))
print("The count of Lower case characters : " + str(res_lower))
