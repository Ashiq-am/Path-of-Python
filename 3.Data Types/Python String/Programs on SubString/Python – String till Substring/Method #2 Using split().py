# Python3 code to demonstrate
# String till Substring
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
# String till Substring
res = test_string.split(spl_word)[0]

# print result
print("String before the substring occurrence : " + res)
