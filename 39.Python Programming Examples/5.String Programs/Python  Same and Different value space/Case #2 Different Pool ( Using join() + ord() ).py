# Python3 code to demonstrate working of
# Same and Different value space
# Different value case

# initializing strings
test_str1 = "abc"

# printing original string
print("The original string is : " + test_str1)

# Using join() + ord() to construct second string
test_str2 = ''.join((chr(idx) for idx in range(97, 100)))

# testing values
res = test_str1 is test_str2

# printing result
print("Are values pointing to same pool ? : " + str(res))
