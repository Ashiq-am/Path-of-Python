# Python3 program to find the longest
# consecutive substring of a certain type
import re


def longestSubstring(str):
    letter = max(re.findall(r'\D+', str), key=len)
    digit = max(re.findall(r'\d+', str), key=len)

    return letter, digit


# Driver Code
str = 'geeks123geeksforgeeks1'
print(longestSubstring(str))
