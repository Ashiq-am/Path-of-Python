# Python3 Program to minimize the
# maximum absolute difference
# between adjacent elements
# of the circular array

# Function to print the reordered array
# which minimizes thee maximum absolute
# difference of adjacent elements
def solve(arr, N):
    # Sort the given array
    arr.sort(reverse=False)

    # Reorder the array
    fl = 1
    k = 0
    for i in range(N // 2 + 1):
        if ((i % 2 and fl) or fl == 0):
            x = arr[i]
            arr.remove(arr[i])
            arr.insert(N - 1 - k, x)
            k += 1
            fl = 0

    # Print the new ordering
    for i in arr:
        print(i, end=" ")


# Driver code
if __name__ == '__main__':
    N = 7

    arr = [1, 3, 10, 2, 0, 9, 6]
    solve(arr, N)
