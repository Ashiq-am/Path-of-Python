# Python implementation to find the sum
# of all composite numbers
# in the given range

# Prefix array to precompute
# the sum of all composite
# number
pref = [0] * 100001


# Function that return number
# num if num is composite
# else return 0
def isComposite(n):
    # Corner cases
    if (n <= 1):
        return 0
    if (n <= 3):
        return 0

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return n
    i = 5
    while (i * i <= n):

        if (n % i == 0 or n % (i + 2) == 0):
            return n
        i = i + 6

    return 0


# Function to precompute the
# sum of all composite numbers
# upto 100000
def preCompute():
    for i in range(1, 100001):
        # checkcomposite()
        # return the number i
        # if i is composite
        # else return 0
        pref[i] = pref[i - 1] + isComposite(i)

    # Function to print the sum


# for each query
def printSum(L, R):
    print(pref[R] - pref[L - 1])


# Function to prsum of all
# composite numbers between
def printSumcomposite(arr, Q):
    # Function that pre computes
    # the sum of all composite
    # numbers
    preCompute()

    # Iterate over all Queries
    # to print the sum
    for i in range(Q):
        printSum(arr[i][0], arr[i][1])

    # Driver code


if __name__ == "__main__":
    Q = 2
    arr = [[10, 13], [12, 21]]

    # Function that print the
    # the sum of all composite
    # number in Range [L, R]
    printSumcomposite(arr, Q)
