# Python3 program to print two strings
# made of character occurring once
# and multiple times

MAX_CHAR = 256


# function to print two strings
# generated from single string one
# with characters occurring onces
# other with character occurring
# multiple of times
def printDuo(string):
    # initialize hashtable with zero
    # entry
    countChar = [0 for i in range(MAX_CHAR)]

    # perform hashing for input string
    n = len(string)
    for i in range(n):
        countChar[ord(string[i]) - ord('a')] += 1

    # generate string (str1) consisting
    # char occurring once and string
    # (str2) consisting char occurring
    # multiple times
    str1 = ""
    str2 = ""
    for i in range(MAX_CHAR):
        if (countChar[i] > 1):
            str2 = str2 + chr(i + ord('a'))
        elif (countChar[i] == 1):
            str1 = str1 + chr(i + ord('a'))

        # print both strings
    print("String with characters occurring once:",
          "\n", str1)
    print("String with characters occurring",
          "multiple times:", "\n", str2)


# Driver Code
string = "lovetocode"
printDuo(string)
