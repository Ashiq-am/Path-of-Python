# Python3 code to demonstrate
# the working of ljust()

lstr = "I love geeksforgeeks"

# Printing the original string
print ("The original string is : \n", lstr, "\n")

# Printing the left aligned
# string with "-" padding
print ("The left aligned string is : ")
print (lstr.ljust(40, '-'))
