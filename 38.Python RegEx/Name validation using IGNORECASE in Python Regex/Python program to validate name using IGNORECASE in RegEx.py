# Python program to validate name using IGNORECASE in RegEx

# Importing re package
import re


def validating_name(name):
    # RegexObject = re.compile( Regular expression, flag )
    # Compiles a regular expression pattern into a regular expression object
    regex_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$',
                            re.IGNORECASE)

    # RegexObject is matched with the desired
    # string using search function
    # In case a match is found, search() returns
    # MatchObject Instance
    # If match is not found, it return None
    res = regex_name.search(name)

    # If match is found, the string is valid
    if res:
        print("Valid")

    # If match is not found, string is invalid
    else:
        print("Invalid")


# Driver Code
validating_name('Mr. Albus Severus Potter')
validating_name('Lily and Mr. Harry Potter')
validating_name('Mr. Cedric')
validating_name('Mr. sirius black')
