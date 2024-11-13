# Python3 program Find concatenated string
# with uncommon characters of given strings
def concatenetedString(s1, s2):
    res = ""  # result
    m = {}

    # store all characters of s2 in map
    for i in range(0, len(s2)):
        m[s2[i]] = 1

    # Find characters of s1 that are not
    # present in s2 and append to result
    for i in range(0, len(s1)):
        if (not s1[i] in m):
            res = res + s1[i]
        else:
            m[s1[i]] = 2

    # Find characters of s2 that are not
    # present in s1.
    for i in range(0, len(s2)):
        if (m[s2[i]] == 1):
            res = res + s2[i]

    return res


# Driver Code
if __name__ == "__main__":
    s1 = "abcs"
    s2 = "cxzca"
    print(concatenetedString(s1, s2))
