# Python3 program to implement
# the above approach

# Function to find the binary by
# performing all the given queries
def toggleQuery(strr, Q, M):
    strr = [i for i in strr]

    # Stores length of the strring
    N = len(strr)

    # prefixCnt[i]: Stores number
    # of times strr[i] toggled by
    # performing all the queries
    prefixCnt = [0] * (N + 1)

    for i in range(M):
        # Update prefixCnt[Q[i][0]]
        prefixCnt[Q[i][0]] += 1

        # Update prefixCnt[Q[i][1] + 1]
        prefixCnt[Q[i][1] + 1] -= 1

    # Calculate prefix sum of prefixCnt[i]
    for i in range(1, N + 1):
        prefixCnt[i] += prefixCnt[i - 1]

    # Traverse prefixCnt[] array
    for i in range(N):

        # If ith element toggled
        # odd number of times
        if (prefixCnt[i] % 2):
            # Toggled i-th element
            # of binary strring
            strr[i] = (chr(ord('1') -
                           ord(strr[i]) +
                           ord('0')))

    return "".join(strr)


# Driver Code
if __name__ == '__main__':
    strr = "101010";
    Q = [[0, 1], [2, 5],
         [2, 3], [1, 4],
         [0, 5]]
    M = len(Q)

    print(toggleQuery(strr, Q, M))
