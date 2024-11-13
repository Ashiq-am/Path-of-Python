# Python program to find the longest
# common prefix between two strings
# after performing swaps on the second string

def LengthLCP(x, y):
    fr = [0] * 26

    a = len(x)  # length of x
    b = len(y)  # length of y

    for i in range(b):
        # creating frequency array of
        # characters of y
        fr[ord(y[i]) - 97] += 1

    # storing the length of
    # longest common prefix
    c = 0

    for i in range(a):
        # checking if the frequency of the character at
        # position i in x in b is greater than zero or not
        # if zero we increase the prefix count by 1
        if (fr[ord(x[i]) - 97] > 0):
            c += 1
            fr[ord(x[i]) - 97] -= 1
        else:
            break
    print(c)


# Driver Code

x, y = "here", "there"

LengthLCP(x, y)
