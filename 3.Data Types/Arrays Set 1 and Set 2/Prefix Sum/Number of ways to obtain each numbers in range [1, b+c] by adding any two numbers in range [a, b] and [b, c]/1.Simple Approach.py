# Python3 program to calculate
# the number of ways
def CountWays(a, b, c):
    x = b + c + 1
    arr = [0] * x

    # Initialising the array with zeros.
    # You can do using memset too.
    for i in range(a, b + 1):
        for j in range(b, c + 1):
            arr[i + j] += 1

    # Printing the array
    for i in range(1, x):
        print(arr[i], end=" ")


# Driver code
if __name__ == '__main__':
    a = 1
    b = 2
    c = 2

    CountWays(a, b, c)

