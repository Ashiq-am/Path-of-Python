# Python3 program to implement
# the above approach

# Function to print the number
# of characters having odd
# frequencies for each query
def queryResult(prefix, Q):
    l = Q[0]
    r = Q[1]

    if (l == 0):
        xorval = prefix[r]
        print(bin(xorval).count('1'))

    else:
        xorval = prefix[r] ^ prefix[l - 1]
        print(bin(xorval).count('1'))

    # A function to construct


# the arr[] and prefix[]
def calculateCount(S, Q, m):
    # Stores array length
    n = len(S)

    # Stores the unique powers of 2
    # associated to each character
    arr = [0] * n
    for i in range(n):
        arr[i] = (1 << (ord(S[i]) - ord('a')))

    # Prefix array to store the
    # XOR values from array elements
    prefix = [0] * n
    x = 0

    for i in range(n):
        x ^= arr[i]
        prefix[i] = x

    for i in range(m):
        queryResult(prefix, Q[i])

    # Driver Code


if __name__ == '__main__':
    S = "geeksforgeeks"

    # Function call
    Q = [[2, 4],
         [0, 3],
         [0, 12]]

    calculateCount(S, Q, 3)
