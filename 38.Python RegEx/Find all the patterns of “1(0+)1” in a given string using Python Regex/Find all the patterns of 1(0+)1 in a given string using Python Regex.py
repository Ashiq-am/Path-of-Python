# Python program to Find all the patterns
# of “1(0+)1” in a given string using Python Regex

import re


# Function to Find all the patterns
# of “1(0+)1” in a given string
def extract(input):
    # search regex '10+1' in original string
    # search() function return first occurrence
    # of regex '10+1' otherwise None
    # '10+1' means sub-string starting and ending with 1
    # and atleast 1 or more zeros in between
    count = 0
    substr = re.search('10+1', input)

    # search for regex in original string
    # untill we are done with complete string
    while substr != None:
        # if we find any occurrence then increase count by 1
        count = count + 1

        # find next occurrence just after previous
        # sub-string
        # for first occurrence 101, substr.start()=1
        # substr.end()=4
        input = input[(substr.end() - 1):]
        substr = re.search('10+1', input)
    print(count)


# Driver program
if __name__ == "__main__":
    input = '1101001'
    extract(input)
