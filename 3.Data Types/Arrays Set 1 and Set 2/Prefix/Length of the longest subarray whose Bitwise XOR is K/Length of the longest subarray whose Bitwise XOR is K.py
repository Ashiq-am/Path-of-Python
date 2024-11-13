# Python3 program to implement
# the above approach

# Function to find the length of the longest
# subarray whose bitwise XOR is equal to K
def LongestLenXORK(arr, N, K):
    # Stores prefix XOR
    # of the array
    prefixXOR = 0

    # Stores length of longest subarray
    # having bitwise XOR equal to K
    maxLen = 0

    # Stores index of prefix
    # XOR of the array
    mp = {}

    # Insert 0 into the map
    mp[0] = -1

    # Traverse the array
    for i in range(N):

        # Update prefixXOR
        prefixXOR ^= arr[i]

        # If (prefixXOR ^ K) present
        # in the map
        if (prefixXOR ^ K) in mp:

            # Update maxLen
            maxLen = max(maxLen,
                         (i - mp[prefixXOR ^ K]))

        # If prefixXOR not present
        # in the Map
        else:

            # Insert prefixXOR
            # into the map
            mp[prefixXOR] = i

    return maxLen


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 4, 7, 2]
    N = len(arr)
    K = 1

    print(LongestLenXORK(arr, N, K))

# This code is contributed by AnkThon
