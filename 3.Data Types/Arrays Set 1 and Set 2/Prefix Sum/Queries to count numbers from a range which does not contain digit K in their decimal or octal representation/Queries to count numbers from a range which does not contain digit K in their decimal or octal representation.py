# Python3 program for the above approach

# Function to check if the given digit
# 'K' is present in the decimal and octal
# representations of num or not
def contains(num, K, base):
    # Stores if the digit exists
    # or not
    isThere = 0

    # Iterate till nums is non-zero
    while (num):

        # Find the remainder
        remainder = num % base

        # If the remainder is K
        if (remainder == K):
            isThere = 1
        num //= base
    return isThere


# Function to count the numbers in the
# range [1, N] such that it doesn't
# contain the digit 'K' in its decimal
# and octal representation
def count(n, k, v):
    # Stores count of numbers in the
    # range [0, i] that contains the
    # digit 'K' in its octal or
    # decimal representation
    pref = [0] * 1000005

    # Traverse the range [0, 1e6 + 5]
    for i in range(1, 10 ** 6 + 5):
        # Check if i contains the digit
        # 'K' in its decimal or
        # octal representation
        present = contains(i, k, 10) or contains(i, k, 8)

        # Update pref[i]
        pref[i] += pref[i - 1] + present

    # Print the answer of queries
    for i in range(n):
        print(v[i][1] - v[i][0] + 1 - (pref[v[i][1]] - pref[v[i][0] - 1]), end=" ")


# Driver Code
if __name__ == '__main__':
    K = 7
    Q = [[2, 5],
         [1, 15]]

    N = len(Q)

    # Function Call
    count(N, K, Q)

# This code is contributed by mohit kumar 29.
