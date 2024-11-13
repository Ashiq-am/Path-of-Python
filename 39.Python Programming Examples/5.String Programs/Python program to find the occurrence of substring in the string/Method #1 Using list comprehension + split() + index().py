# Python3 code to demonstrate working of
# Word occurrence positions in String
# Using list comprehension + split() + index()

# initializing string
test_str = 'geeksforgeeks is best for geeks and cs'

# printing original string
print("The original string is : " + str(test_str))

# initializing list
test_list = ["best", "geeks", "cs"]

# using index() to get indices,
# list comprehension used to offer one liner
res = [test_str.split().index(ele)
       for ele in test_str.split() if ele in test_list]

# printing result
print("The indices list : " + str(res))
