# Python3 code to demonstrate
# Get String after substring occurrence
# using split()

# initializing string
test_string = "GeeksforGeeks is best for geeks"

# initializing split word
spl_word = 'best'

# printing original string
print("The original string : " + str(test_string))

# printing split string
print("The split string : " + str(spl_word))

# using split()
# Get String after substring occurrence
res = test_string.partition(spl_word)[2]

# print result
print("String after the substring occurrence : " + res)
