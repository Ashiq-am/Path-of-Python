# Python program that matches a word
# containing ‘g’ followed by one or
# more e’s using regex

# import re packages
import re


# Function check if the any word of
# the string containing 'g' followed
# by one or more e's
def check(string):
    # Regex \w * ge+\w * will match
    # text that contains 'g', followed
    # by one or more 'e'
    regex = re.compile("ge+\w*")

    # The findall() method returns all
    # matching strings of the regex pattern
    match_object = regex.findall(string)

    # If length of match_object is not
    # equal to zero then it contains
    # matched string
    if len(match_object) != 0:

        # looping through the list
        for word in match_object:
            print(word)

    else:
        print("No match")

    # Driver Code


if __name__ == '__main__':
    # Enter the string
    string = "Welcome to geeks for geeks"

    # Calling check function
    check(string)
