# Python program to check input is
# Floating point number or not

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression for
# identifying Floating point number
regex = '[+-]?[0-9]+\.[0-9]+'


# Define a function to
# check Floating point number
def check(floatnum):
    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, floatnum)):
        print("Floating point number")

    else:
        print("Not a Floating point number")

    # Driver Code


if __name__ == '__main__':
    # Enter the floating point number
    floatnum = "1.20"

    # calling run function
    check(floatnum)

    floatnum = "-2.356"
    check(floatnum)

    floatnum = "0.2"
    check(floatnum)

    floatnum = "-3"
    check(floatnum)
