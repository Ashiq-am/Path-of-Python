# Python code to implement the above approach
pre = [0] * (100001)


def CheckZero(x):
    s = str(x)
    i = 0
    n = len(s)

    # To check leading zero
    while (i < n and s[i] == '0'):
        i += 1

    # Check remaining digits
    while (i < n):
        if (s[i] == '0'):
            return True
        i += 1

    return False


# Function to precompute sum of duck numbers from 1 to i
def precompute():
    for i in range(1, 100001):
        if (CheckZero(i)):
            pre[i] = pre[i - 1] + i
        else:
            pre[i] = pre[i - 1]


# Function to print sum of duck numbers in range [L, R]
def printresult(L, R):
    print(pre[R] - pre[L - 1])


def printsumduck(arr, Q):
    # To calculate pre array
    precompute()
    for i in range(Q):
        # arr[i][0] is L and arr[i][1] is R
        printresult(arr[i][0], arr[i][1])


Q = 5
arr = [[1, 10],
       [99, 121],
       [56, 70],
       [1000, 1111],
       [108, 250]]

# Function call
printsumduck(arr, Q)

# This code is contributed by lokeshmvs21.
