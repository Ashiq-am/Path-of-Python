# Python3 program to implement
# the above appraoch

# Function to get the count
# of triples that satisfy
# the given condition
def cntTriplet(arr, N):
    # preZero[i] stores count
    # of 0 up to index i
    preZero = [0] * N

    # Traverse the array and
    # Count 0s up to index i
    for i in range(N):
        if (arr[i] == 0):
            preZero[i] = preZero[
                             max(i - 1, 0)] + 1
        else:
            preZero[i] = preZero[
                max(i - 1, 0)]

    # Stores count of triplet that
    # satisfy the given conditions
    tripletCount = 0

    # Traverse the given array
    for i in range(N):
        if (arr[i] == 0):

            # Stores count of elements
            # on the left side of arr[i]
            X = i

            # Stores count of elements
            # on the right side of arr[i]
            Y = N - i - 1

            tripletCount += X * Y

        else:

            # Stores count of 0s on
            # the left side of arr[i]
            X = preZero[i]

            # Stores count of 0s on
            # the right side of arr[i]
            Y = preZero[N - 1] - preZero[i]

            tripletCount += X * Y

    return tripletCount


# Driver code
if __name__ == '__main__':
    arr = [1, 0, 2, 3]
    N = len(arr)

    print(cntTriplet(arr, N))
