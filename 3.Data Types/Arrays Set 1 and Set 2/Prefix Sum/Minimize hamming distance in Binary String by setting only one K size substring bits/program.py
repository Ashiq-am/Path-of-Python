# Py program for the above approach

# Function to find minimum Hamming
# Distance after atmost one operation
def minimumHammingDistance(S, K):
    # Store the size of the string
    n = len(S)

    # Store the prefix sum of 1s
    pref = [0] * n

    # Create Prefix Sum array
    pref[0] = ord(S[0]) - ord('0')
    for i in range(1, n):
        pref[i] = pref[i - 1] + (ord(S[i]) - ord('0'))

    # Initialize cnt as number of ones
    # in string S
    cnt = pref[n - 1]

    # Store the required result
    ans = cnt

    # Traverse the string, S
    for i in range(n - K):
        # Store the number of 1s in the
        # subtring S[i, i+K-1]
        value = pref[i + K - 1] - (pref[i - 1] if (i - 1) >= 0 else 0)

        # Update the answer
        ans = min(ans, cnt - value + (K - value))

    # Return the result
    return ans


# Driver Code
if __name__ == '__main__':
    # Given Input
    s = "101"
    K = 2

    # Function Call
    print(minimumHammingDistance(s, K))
