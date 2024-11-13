# Python3 code to demonstrate working of
# Same and Different value space
# Same value case

# initializing strings
test_str1 = "gfg"

# printing original string
print("The original string is : " + test_str1)

# Using + to construct second string
test_str2 = "g" + "fg"

# testing values
res = test_str1 is test_str2

# printing result
print("Are values pointing to same pool ? : " + str(res))
