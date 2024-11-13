# Python3 program to replace c1 with c2
# and c2 with c1
def replace(s, c1, c2):
    l = len(s)

    # loop to traverse in the string
    for i in range(l):

        # check for c1 and replace
        if (s[i] == c1):
            s = s[0:i] + c2 + s[i + 1:]

        # check for c2 and replace
        elif (s[i] == c2):
            s = s[0:i] + c1 + s[i + 1:]
    return s


# Driver Code
if __name__ == '__main__':
    s = "grrksfoegrrks"
    c1 = 'e'
    c2 = 'r'
    print(replace(s, c1, c2))
