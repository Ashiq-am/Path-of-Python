# Python implementation of substituting
# a character set with a specific character

# importing regex module
import re


# Function to perform
# operations on the strings
def substitutor():
    # a string variable
    sentence = "22 April is celebrated as Earth Day."

    # replacing every lower case characters
    # in the variable sentence with 0 and
    # printing the modified string
    print(re.sub(r"[a-z]", "0", sentence))


# Driver Code:
substitutor()
