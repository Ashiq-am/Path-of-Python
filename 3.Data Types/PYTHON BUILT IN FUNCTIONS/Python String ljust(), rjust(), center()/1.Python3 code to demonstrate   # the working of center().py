# Python3 code to demonstrate
# the working of center()

cstr = "I love geeksforgeeks"

# Printing the original string
print ("The original string is : \n", cstr, "\n")

# Printing the center aligned string
print ("The center aligned string is : ")
print (cstr.center(40), "\n")

# Printing the center aligned
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
