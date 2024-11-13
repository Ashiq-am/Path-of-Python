# Python3 program to find longest
# string which is prefix string
# of at least two strings

max1 = 0


# Function to find max length
# of the prefix
def MaxLength(v, i, m):
    global max1

    # Base case
    if (i >= m):
        return m - 1

    # Iterating over all the alphabets
    for k in range(26):
        c = chr(ord('a') + k)
        v1 = []

        # Checking if char exists in
        # current string or not
        for j in range(len(v)):
            if (v[j][i] == c):
                v1.append(v[j])

        # If atleast 2 string have
        # that character
        if (len(v1) >= 2):

            # Recursive call to i+1
            max1 = max(max1, MaxLength(v1, i + 1, m))
        else:
            max1 = max(max1, i - 1)

    return max1


# Driver code
if __name__ == '__main__':
    # Initialising strings
    s1 = "abcde"
    s2 = "abcsd"
    s3 = "bcsdf"
    s4 = "abcda"
    s5 = "abced"
    v = []

    # Push strings into vectors.
    v.append(s1)
    v.append(s2)
    v.append(s3)
    v.append(s4)
    v.append(s5)

    m = len(v[0])

    print(MaxLength(v, 0, m) + 1)

# This code is contributed by BhupendraSingh
