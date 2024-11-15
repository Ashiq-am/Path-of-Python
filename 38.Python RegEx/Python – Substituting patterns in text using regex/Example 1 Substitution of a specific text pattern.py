# Python implementation of substituting a
# specific text pattern in a string using regex

# importing regex module
import re


# Function to perform
# operations on the strings
def substitutor():
    # a string variable
    sentence1 = "It is raining outside."

    # replacing text 'raining' in the string
    # variable sentence1 with 'sunny' thus
    # passing first parameter as raining
    # second as sunny, third as the
    # variable name in which string is stored
    # and printing the modified string
    print(re.sub(r"raining", "sunny", sentence1))

    # a string variable
    sentence2 = "Thank you very very much."

    # replacing text 'very' in the string
    # variable sentence2 with 'so' thus
    # passing parameters at their
    # appropriate positions and printing
    # the modified string
    print(re.sub(r"very", "so", sentence2))


# Driver Code:
substitutor()
