# Python3 code to demonstrate working of
# Alternate cases in String
# Using list comprehension

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + str(test_str))

# Using list comprehension
# Alternate cases in String
res = [ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(test_str)]
res = "".join(res)

# printing result
print("The alterate case string is : " + str(res))
