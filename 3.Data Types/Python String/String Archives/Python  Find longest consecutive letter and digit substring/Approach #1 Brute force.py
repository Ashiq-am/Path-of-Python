# Python3 program to find the longest
# consecutive substring of a certain type
import re


def longestSubstring(s):
    longest_letterSeq = ''
    longest_digitSeq = ''
    i = 0
    while (i < len(s)):

        curr_letterSeq = ''
        curr_digitSeq = ''

        # For letter substring
        while (i < len(s) and s[i].isalpha()):
            curr_letterSeq += s[i]
            i += 1

        # For digit substring
        while (i < len(s) and s[i].isdigit()):
            curr_digitSeq += s[i]
            i += 1

        # Case handling if the character
        # is neither letter nor digit
        if (i < len(s) and not (s[i].isdigit())
                and not (s[i].isalpha())):
            i += 1

        if (len(curr_letterSeq) > len(longest_letterSeq)):
            longest_letterSeq = curr_letterSeq

        if (len(curr_digitSeq) > len(longest_digitSeq)):
            longest_digitSeq = curr_digitSeq

    return longest_letterSeq, longest_digitSeq


# Driver Code
str = '3Geeksfor123geeks3'
print(longestSubstring(str))
