# Space optimized Python3 implementation to
# print longest common substring.

# Function to find longest common substring.
def LCSubStr(X, Y):
    # Find length of both the strings.
    m = len(X)
    n = len(Y)

    # Variable to store length of longest
    # common substring.
    result = 0

    # Variable to store ending point of
    # longest common substring in X.
    end = 0

    # Matrix to store result of two
    # consecutive rows at a time.
    length = [[0 for j in range(m)]
              for i in range(2)]

    # Variable to represent which row of
    # matrix is current row.
    currRow = 0

    # For a particular value of i and j,
    # length[currRow][j] stores length
    # of longest common substring in
    # string X[0..i] and Y[0..j].
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if (i == 0 or j == 0):
                length[currRow][j] = 0

            elif (X[i - 1] == Y[j - 1]):
                length[currRow][j] = length[1 - currRow][j - 1] + 1

                if (length[currRow][j] > result):
                    result = length[currRow][j]
                    end = i - 1
            else:
                length[currRow][j] = 0

        # Make current row as previous row and
        # previous row as new current row.
        currRow = 1 - currRow

    # If there is no common substring, print -1.
    if (result == 0):
        return "-1"

    # Longest common substring is from index
    # end - result + 1 to index end in X.
    return X[end - result + 1: end + 1]


# Driver code
if __name__ == "__main__":
    X = "GeeksforGeeks"
    Y = "GeeksQuiz"

    # Function call
    print(LCSubStr(X, Y))
