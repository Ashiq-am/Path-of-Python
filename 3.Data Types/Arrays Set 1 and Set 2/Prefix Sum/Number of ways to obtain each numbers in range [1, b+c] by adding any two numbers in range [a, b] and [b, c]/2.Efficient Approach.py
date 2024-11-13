# Python3 program to calculate
# the number of ways
def CountWays(a, b, c):
    # 2 is added because sometimes
    # we will decrease the
    # value out of bounds.
    x = b + c + 2

    # Initialising the array with zeros.
    arr = [0] * x

    for i in range(1, b + 1):
        arr[i + b] = arr[i + b] + 1
    arr[i + c + 1] = arr[i + c + 1] - 1

    # Printing the array
    for i in range(1, x - 1):

        arr[i] += arr[i - 1]
        print(arr[i], end=" ")


# Driver code
if __name__ == '__main__':
    a = 1
    b = 2
    c = 2

    CountWays(a, b, c)


