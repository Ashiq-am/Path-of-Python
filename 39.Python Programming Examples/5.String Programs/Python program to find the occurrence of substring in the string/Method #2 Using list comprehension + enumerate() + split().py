# Python3 code to demonstrate working of
# Word occurrence positions in String
# Using list comprehension + enumerate() + split()

# initializing string
test_str = 'geeksforgeeks is best for geeks and cs'

# printing original string
print("The original string is : " + str(test_str))

# initializing list
test_list = ["best", "geeks", "cs"]

# using enumerate() to get indices,
# list comprehension used to offer one liner
res = [idx for idx, ele in enumerate(test_str.split()) if ele in test_list]

# printing result
print("The indices list : " + str(res))
