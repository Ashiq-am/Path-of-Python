# Python3 code to demonstrate
# Find last occurrence of substring
# using rfind()

# initializing string
test_string = "GfG is best for CS and also best for Learning"

# initializing target word
tar_word = "best"

# printing original string
print("The original string : " + str(test_string))

# using rfind()
# Find last occurrence of substring
res = test_string.rfind(tar_word)

# print result
print("Index of last occurrence of substring is : " + str(res))
