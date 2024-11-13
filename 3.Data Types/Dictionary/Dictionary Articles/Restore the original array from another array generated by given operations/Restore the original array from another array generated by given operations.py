def solve(n, k, arr):
    # Initialize 'flag' to True
    flag = True

    # Initialize 'lastindex' to the index of the last
    # element in the array
    lastindex = n - 1

    # Iterate for a maximum of min(n, k) times to prevent
    # exceeding array bounds
    for i in range(min(n, k)):
        # Check if the element at the current 'lastindex'
        # is greater than n
        if arr[lastindex] > n:
            # If true, set 'flag' to False and break out of
            # the loop
            flag = False
            break

        # Calculate the distance needed to move 'lastindex'
        # to a new position based on the current element
        dist = n - arr[lastindex]

        # Update 'lastindex' accordingly, moving dist steps
        # clockwise in the array
        lastindex = (lastindex + dist) % n

    # Output the result based on the value of 'flag'
    if flag:
        print("Yes")
    else:
        print("No")


# Driver Code
n = 5
k = 3
arr = [4, 3, 3, 2, 3]

solve(n, k, arr)
