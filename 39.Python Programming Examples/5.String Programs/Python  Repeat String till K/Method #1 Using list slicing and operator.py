# Python3 code to demonstrate
# Repeat string till K
# using list slicing and // operator

# initializing string
test_string = "GeeksforGeeks"

# initializing K
K = 30

# printing original string
print("The original string : " + str(test_string))

# using list slicing and // operator
# Repeat string till K
res = (test_string * (K//len(test_string)+ 1))[:K]

# print result
print("String after performing repeatition : " + res)
