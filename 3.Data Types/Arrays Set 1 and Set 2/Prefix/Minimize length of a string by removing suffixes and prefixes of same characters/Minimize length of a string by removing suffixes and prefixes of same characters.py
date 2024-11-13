# Python3 program for the above approach

# Function to find the minimum length
# of the string after removing the same
# characters from the end and front of the
# two strings after dividing into 2 substrings
def minLength(s):
    # Initialize two pointers
    i = 0;
    j = len(s) - 1

    # Traverse the string S
    while (i < j and s[i] == s[j]):

        # Current char on left pointer
        d = s[i]

        # Shift i towards right
        while (i <= j and s[i] == d):
            i += 1

        # Shift j towards left
        while (i <= j and s[j] == d):
            j -= 1

    # Return the minimum possible
    # length of string
    return j - i + 1


# Driver Code
if __name__ == "__main__":
    S = "aacbcca"

    print(minLength(S))

# This code is contributed by AnkThon
