# Python code to demonstrate
# split string to character list
# using map()

# initializing string
test_string = 'GeeksforGeeks'

# printing the original string
print ("The original string is : " + str(test_string))

# using map()
# to split string to character list
res = list(map(None, test_string))

# printing result
print ("The splitted character's list is : " + str(res))
