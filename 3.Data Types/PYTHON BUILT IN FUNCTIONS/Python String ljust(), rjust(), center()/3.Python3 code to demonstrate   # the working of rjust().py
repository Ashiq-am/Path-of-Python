# Python3 code to demonstrate
# the working of rjust()

rstr = "I love geeksforgeeks"

# Printing the original string
print ("The original string is : \n", rstr, "\n")

# Printing the right aligned string
# with "-" padding
print ("The right aligned string is : ")
print (rstr.rjust(40, '-'))
