# Python program to identify the Digit

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for identifying a digit
regex = '^[0-9]+$'


# Define a function for
# identifying a Digit
def check(string):
    # pass the regualar expression
    # and the string in search() method
    if (re.search(regex, string)):
        print("Digit")

    else:
        print("Not a Digit")

    # Driver Code


if __name__ == '__main__':
    # Enter the string
    string = "28"

    # calling run function
    check(string)

    string = "a"
    check(string)

    string = "21ab"
    check(string)

    string = "12ab12"
    check(string)
