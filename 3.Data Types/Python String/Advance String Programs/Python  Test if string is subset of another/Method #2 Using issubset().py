# Python3 code to demonstrate working of
# Test if string is subset of another
# Using issubset()

# initializing strings
test_str1 = "geeksforgeeks"
test_str2 = "gfks"

# printing original string
print("The original string is : " + test_str1)

# Test if string is subset of another
# Using issubset()
res = set(test_str2).issubset(test_str1)

# printing result
print("Does string contains all the characters of other list? : " + str(res))
