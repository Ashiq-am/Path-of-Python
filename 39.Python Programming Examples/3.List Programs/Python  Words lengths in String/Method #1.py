# Python3 code to demonstrate
# Words lengths in String
# using split()

# initializing string
test_string = "Geeksforgeeks is best Computer Science Portal"

# printing original string
print ("The original string is : " + test_string)

# using split()
# Words lengths in String
res = list(map(len, test_string.split()))

# printing result
print ("The list of words lengths is : " + str(res))
