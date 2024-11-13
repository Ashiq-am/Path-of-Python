# Python implementation of case-insensitive substitution
# of a character set with a specific character

# importing regex module
import re


# Function to perform
# operations on the strings
def substitutor():
    # a string variable
    sentence = "22 April is celebrated as Earth Day."

    # replacing both lowercase and
    # uppercase characters with 0 in
    # the variable sentence by using
    # flag and printing the modified string
    print(re.sub(r"[a-z]", "0", sentence, flags=re.I))


# Driver Code:
substitutor()
