# Python implementation to perform substitution
# up to a certain number of characters

# importing regex module
import re


# Function to perform
# operations on the strings
def substitutor():
    # a string variable
    sentence = "Follow your Passion."

    # case-insensitive substitution
    # on variable sentence upto
    # eight characters and printing
    # the modified string
    print(re.sub(r"[a-z]", "0", sentence, 8, flags=re.I))


# Driver Code:
substitutor()
