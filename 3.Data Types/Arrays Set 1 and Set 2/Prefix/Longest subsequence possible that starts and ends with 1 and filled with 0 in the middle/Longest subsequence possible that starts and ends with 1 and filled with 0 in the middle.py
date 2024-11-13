# Python3 program to find the
# longest subsequence possible
# that starts and ends with 1
# and filled with 0 in the middle
import sys


def longestSubseq(s, length):
    # Prefix array to store the
    # occurrences of '1' and '0'
    # Initialise prefix arrays with 0
    ones = [0 for i in range(length + 1)]
    zeroes = [0 for i in range(length + 1)]

    # Iterate over the length of the string
    for i in range(length):

        # If current character is '1'
        if (s[i] == '1'):
            ones[i + 1] = ones[i] + 1
            zeroes[i + 1] = zeroes[i]

        # If current character is '0'
        else:
            zeroes[i + 1] = zeroes[i] + 1
            ones[i + 1] = ones[i]

    answer = -sys.maxsize - 1
    x = 0

    for i in range(length + 1):
        for j in range(i, length + 1):
            # Add '1' available for
            # the first string
            x += ones[i]

            # Add '0' available for
            # the second string
            x += (zeroes[j] - zeroes[i])

            # Add '1' available for
            # the third string
            x += (ones[length] - ones[j])

            # Update answer
            answer = max(answer, x)
            x = 0

    # Print the final result
    print(answer)


# Driver Code
S = "10010010111100101"
length = len(S)

longestSubseq(S, length)

# This code is contributed by avanitrachhadiya2155
