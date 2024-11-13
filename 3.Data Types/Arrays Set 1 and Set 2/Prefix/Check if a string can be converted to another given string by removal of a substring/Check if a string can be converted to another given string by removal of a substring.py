# Python program for the above approach

# Function to check if S can be converted to T
# by removing at most one substring from S
def make_string_S_to_T(S, T):
    # Check if S can be converted to T by
    # removing at most one substring from S
    possible = False

    # Stores length of string T
    M = len(T)

    # Stores length of string S
    N = len(S)

    # Iterate over the range [0, M - 1]
    for i in range(0, M + 1):

        # Stores Length of the substring
        # S[0], ..., S[i]
        prefix_length = i

        # Stores Length of the substring
        # S[0], ..., S[i]
        suffix_length = M - i

        # Stores prefix substring
        prefix = S[:prefix_length]

        # Stores suffix substring
        suffix = S[N - suffix_length:N]

        # Checking if prefix+suffix == T
        if (prefix + suffix == T):
            possible = True
            break

    if (possible):
        return "YES"
    else:
        return "NO"


# Driver Code

# Given String S and T
S = "ababcdcd"
T = "abcd"

# Function call
print(make_string_S_to_T(S, T))

# This code is contributed by shubhamsingh10
