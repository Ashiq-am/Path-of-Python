# Python 3 code to demonstrate
# First character occurrence from rear String
# using rfind()

# initializing string
test_str = "Geeksforgeeks"

# printing original string
print ("The original string is : " + str(test_str))

# using rfind()
# to get last element occurrence
res = test_str.rfind('e')

# printing result
print ("The index of last element occurrence: " + str(res))
