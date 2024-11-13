"""In this output is formatted by using string slicing and concatenation operations.
The string type has some methods that help in formatting a output in an fancier way.
Some of method which help in formatting a output are str.ljust(), str.rjust(), str.centre()"""

# Python program to
# format a output using
# string() method

cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))
