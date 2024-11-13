# Python3 program for the
# above approach
MAX = 1000050

# Array to store smallest
# prime factors of each no.
spf = [0 for i in range(MAX + 1)]


# Function to calculate smallest
# prime factor of N.
def calculate_SPF():
    for i in range(MAX + 1):
        spf[i] = i

    for i in range(4, MAX + 1, 2):
        spf[i] = 2

    i = 3

    while (i * i <= MAX):
        if (spf[i] == i):

            j = i * i

            while (j <= MAX):

                # Marking spf[j] if
                # it is not previously
                # marked
                if (spf[j] == j):
                    spf[j] = i

                j += i
        i += 1


# Array to store the
# count of factor for N
tfactor = [0 for i in range(MAX + 1)]

# Prefix array which contains
# the count of factors from 1 to N
pre = [0 for i in range(MAX + 1)]


# Function to count
# total factors from 1 to N
def CountTotalfactors():
    tfactor[1] = pre[1] = 1

    for i in range(2, MAX + 1):
        mspf = spf[i]
        prim = mspf
        temp = i
        cnt = 0

        while (temp % mspf == 0):
            temp //= mspf
            cnt += 1
            prim = prim * mspf

        # Store total factors of i
        tfactor[i] = (cnt + 1) * tfactor[temp]

    # Stores total factors
    # from 1 to i
    pre[i] = pre[i - 1] + tfactor[i]


# Function to search lowest X
# such that the given condition
# is satisfied
def BinarySearch(X):
    start = 1
    end = MAX - 1

    while (start < end):

        # Find mid
        mid = (start + end) // 2

        if (pre[mid] == X):
            return mid

        # Search in the right half
        elif (pre[mid] < X):
            start = mid + 1

        # Search in the left half
        else:
            end = mid

        # Return the position after
    # Binary Search
    return start


# Function to find the
# required sum
def findSumOfCount(X):
    # Precompute smallest prime
    # factor of each value
    calculate_SPF()

    # Calculate count of total
    # factors from 1 to N
    CountTotalfactors()

    # Binary search to find
    # minimum N
    print(BinarySearch(X))


# Driver code
if __name__ == "__main__":
    # Given Sum
    X = 10

    # Function Call
    findSumOfCount(X)


