# Python3 code to demonstrate
# Repeat string till K
# using divmod() + list slicing

# initializing string
test_string = "GeeksforGeeks"

# initializing K
K = 30

# printing original string
print("The original string : " + str(test_string))

# using divmod() + list slicing
# Repeat string till K
div, mod = divmod(K, len(test_string))
res = test_string * div + test_string[:mod]

# print result
print("String after performing repeatition : " + res)
