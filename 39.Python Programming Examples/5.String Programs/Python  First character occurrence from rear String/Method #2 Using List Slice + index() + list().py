# Python 3 code to demonstrate
# First character occurrence from rear String
# using List Slice + index() + list()

# initializing string
test_str = "Geeksforgeeks"

# printing original string
print ("The original string is : " + str(test_str))

# using List Slice + index() + list()
# First character occurrence from rear String
test_str = list(test_str)
res = len(test_str) - 1 - test_str[::-1].index('e')

# printing result
print ("The index of last element occurrence: " + str(res))
