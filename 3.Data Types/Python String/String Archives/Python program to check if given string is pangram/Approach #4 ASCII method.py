# Python3 program to
# Check if the string is pangram
import itertools
import string

alphabet = set(string.ascii_lowercase)


def ispangram(str):
    return sum(1 for i in set(str) if 96 < ord(i) <= 122) == 26


# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if (ispangram(string) == True):
    print("Yes")
else:
    print("No")
