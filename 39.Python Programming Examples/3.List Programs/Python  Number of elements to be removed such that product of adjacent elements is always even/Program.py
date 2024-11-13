# Python 3 implementation of the
# above approach

# Function to find minimum number of
# eliminations such that product of all
# adjacent elements is even
def min_elimination(n, arr):
    countOdd = 0
    counteven = 0
    # Stores the new value
    for i in range(n):

        # Count odd and even numbers
        if (arr[i] % 2):
            countOdd += 1
        else:
            counteven += 1
    # if all are even
    if counteven == n:
        return 0

    # if all are odd
    if countOdd == n:
        return n
    else:
        countpair = 0
        for i in range(1, n):
            if (arr[i] % 2 == 1 and arr[i - 1] % 2 == 1):
                countpair += 1
        return countpair


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 7, 9]
    n = len(arr)

    print(min_elimination(n, arr))
