# Python3 code to demonstrate working of
# Eliminate Capital Letter Starting words from String
# Using join() + split() + isupper()

# initializing string
test_str = 'GeeksforGeeks is Best for Geeks'

# printing original string
print("The original string is : " + str(test_str))

# Eliminate Capital Letter Starting words from String
# Using join() + split() + isupper()
temp = test_str.split()
res = " ".join([ele for ele in temp if not ele[0].isupper()])

# printing result
print("The filtered string : " + str(res))
