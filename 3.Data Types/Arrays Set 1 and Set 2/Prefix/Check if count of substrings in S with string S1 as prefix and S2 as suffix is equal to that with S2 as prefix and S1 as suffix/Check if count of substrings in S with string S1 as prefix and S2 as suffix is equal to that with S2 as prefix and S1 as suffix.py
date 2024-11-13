# Python3 program for the above approach

# Function to count number of
# substrings that starts with
# string S1 and ends with string S2
def countSubstrings(S, S1, S2):
    # Stores the length of each string
    N = len(S)
    N1 = len(S1)
    N2 = len(S2)

    # Stores the count of prefixes
    # as S1 and suffixes as S2
    count = 0
    totalcount = 0

    # Traverse string S
    for i in range(N):

        # Find the prefix at index i
        prefix = S[i: (i + N1) if (i + N1 < N) else N]

        # Find the suffix at index i
        suffix = S[i: (i + N2) if (i + N2 < N) else N]

        # If the prefix is S1
        if S1 == prefix:
            count += 1

        # If the suffix is S2
        if S2 == suffix:
            totalcount += count

    # Return the count of substrings
    return totalcount


# Function to check if the number of
# substrings starts with S1 and ends
# with S2 and vice-versa is same or not
def checkSubstrings(S, S1, S2):
    x = countSubstrings(S, S1, S2)
    y = countSubstrings(S, S2, S1)

    if x == y:
        print("Yes")
    else:
        print("No")


# Driver code
S = "opencloseopencloseopen"
S1 = "open"
S2 = "close"

checkSubstrings(S, S1, S2)

# This code is contributed by abhinavjain194
