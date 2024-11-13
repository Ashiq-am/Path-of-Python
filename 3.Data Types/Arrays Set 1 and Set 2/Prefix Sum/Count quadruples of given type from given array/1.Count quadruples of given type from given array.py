# Python3 program of the
# above approach

maxN = 2002

# lcount[i][j]: Stores the
# count of i on left of index j
lcount = [[0 for i in range(maxN)] for j in range(maxN)]

# rcount[i][j]: Stores the
# count of i on right of index j
rcount = [[0 for i in range(maxN)] for j in range(maxN)]


# Function to count unique
# elements on left and right
# of any index
def fill_counts(a, n):
    # Find the maximum
    # array element
    maxA = a[0]

    for i in range(n):
        if (a[i] > maxA):
            maxA = a[i]

    for i in range(n):
        lcount[a[i]][i] = 1
        rcount[a[i]][i] = 1

    for i in range(maxA + 1):

        # Calculate prefix sum of
        # counts of each value
        for j in range(1, n):
            lcount[i][j] = lcount[i][j - 1] + lcount[i][j]

        # Calculate suffix sum of
        # counts of each value
        for j in range(n - 2, 0, -1):
            rcount[i][j] = rcount[i][j + 1] + rcount[i][j]


# Function to count quadruples
# of the required type
def countSubsequence(a, n):
    fill_counts(a, n)
    answer = 0
    for i in range(1, n):
        for j in range(i + 1, n - 1):
            answer += lcount[a[j]][i - 1] * rcount[a[i]][j + 1]

    return answer


# Driver Code
if __name__ == '__main__':
    a = [1, 2, 3, 2, 1, 3, 2]
    print(countSubsequence(a, len(a)))
