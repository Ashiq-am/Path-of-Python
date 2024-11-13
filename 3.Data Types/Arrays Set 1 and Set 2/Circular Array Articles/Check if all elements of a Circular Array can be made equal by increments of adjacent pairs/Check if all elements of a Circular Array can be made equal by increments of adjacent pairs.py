# Python3 program to implement
# the above approach

# Function to check if all array
# elements can be made equal
def checkEquall(arr, N):
    # Stores the sum of even and
    # odd array elements
    sumEven, sumOdd = 0, 0

    for i in range(N):

        # If index is odd
        if (i & 1):
            sumOdd += arr[i]
        else:
            sumEven += arr[i]

    if (sumEven == sumOdd):
        return True
    else:
        return False


# Driver Code
if __name__ == "__main__":

    arr = [2, 7, 3, 5, 7]
    N = len(arr)

    if (checkEquall(arr, N)):
        print("YES")
    else:
        print("NO")
