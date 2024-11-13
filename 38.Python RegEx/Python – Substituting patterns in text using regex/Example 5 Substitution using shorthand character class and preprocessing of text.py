# Python implementation of Substitution using
# shorthand character class and preprocessing of text

# importing regex module
import re


# Function to perform
# operations on the strings
def substitutor():
    # list of strings
    S = ["2020 Olympic games have @# been cancelled",
         "Dr Vikram Sarabhai was +%--the ISRO’s first chairman",
         "Dr Abdul		 Kalam, the father	 of India's missile programme"]

    # loop to iterate every element of list
    for i in range(len(S)):
        # replacing every non-word character with a white space
        S[i] = re.sub(r"\W", " ", S[i])

        # replacing every digit character with a white space
        S[i] = re.sub(r"\d", " ", S[i])

        # replacing one or more white space with a single white space
        S[i] = re.sub(r"\s+", " ", S[i])

        # replacing alphabetic characters which have one or more
        # white space before and after them with a white space
        S[i] = re.sub(r"\s+[a-z]\s+", " ", S[i], flags=re.I)

        # substituting one or more white space which is at
        # beginning of the string with an empty string
        S[i] = re.sub(r"^\s+", "", S[i])

        # substituting one or more white space which is at
        # end of the string with an empty string
        S[i] = re.sub(r"\s+$", "", S[i])

    # loop to iterate every element of list
    for i in range(len(S)):
        # printing each modified string
        print(S[i])

    # Driver Code:


substitutor()
