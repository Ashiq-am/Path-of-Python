# Python3 program for the above approach

# Function to print the count of all
# prefix in the given string
def Print(occ, s):
    # Iterate over string s
    for i in range(1, len(s) + 1):
        # Print the prefix and their
        # frequency
        print(s[0: i], "occur", occ[i], "times.")


# Function to implement the LPS
# array to store the longest prefix
# which is also a suffix for every
# substring of the string S
def prefix_function(s):
    # Array to store LPS values
    # Value of lps[0] is 0
    # by definition
    LPS = [0 for i in range(len(s))]

    # Find the values of LPS[i] for
    # the rest of the string using
    # two pointers and DP
    for i in range(1, len(s)):

        # Initially set the value
        # of j as the longest
        # prefix that is also a
        # suffix for i as LPS[i-1]
        j = LPS[i - 1]

        # Check if the suffix of
        # length j+1 is also a prefix
        while (j > 0 and s[i] != s[j]):
            j = LPS[j - 1]

        # If s[i] = s[j] then, assign
        # LPS[i] as j+1
        if (s[i] == s[j]):
            LPS[i] = j + 1

        # If we reached j = 0, assign
        # LPS[i] as 0 as there was no
        # prefix equal to suffix
        else:
            LPS[i] = 0

    # Return the calculated
    # LPS array
    return LPS


# Function to count the occurrence
# of all the prefix in the string S
def count_occurrence(s):
    n = len(s)

    # Call the prefix_function
    # to get LPS
    LPS = prefix_function(s)

    # To store the occurrence of
    # all the prefix
    occ = [0 for i in range(n + 1)]

    # Count all the suffixes that
    # are also prefix
    for i in range(n):
        occ[LPS[i]] += 1

    # Add the occurrences of
    # i to smaller prefixes
    for i in range(n - 1, 0, -1):
        occ[LPS[i - 1]] += occ[i]

    # Adding 1 to all occ[i] for all
    # the original prefix
    for i in range(n + 1):
        occ[i] += 1

    # Function Call to print the
    # occurrence of all the prefix
    Print(occ, s)


# Driver Code

# Given String
A = "ABACABA"

# Function Call
count_occurrence(A)

# This code is contributed by avanitrachhadiya2155
