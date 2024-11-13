# Python 3 program for the above approach

# Function to find the minimum number
# of moves required to make all array
# elements equal
def findMinMoves(arr, N):
    # Store the total sum of the array
    sum = 0

    # Calculate total sum of the array
    for i in range(N):
        sum += arr[i]

    # If the sum is not divisible
    # by N, then print "-1"
    if (sum % N != 0):
        return -1

    # Stores the average
    avg = sum // N

    # Stores the count
    # of operations
    total = 0
    needCount = 0

    # Traverse the array arr[]
    for i in range(N):
        # Update number of moves
        # required to make current
        # element equal to avg
        needCount += (arr[i] - avg)

        # Update the overall count
        total = max(max(abs(needCount), arr[i] - avg), total)

    # Return the minimum
    # operations required
    return total


# Driver Code
if __name__ == '__main__':
    arr = [1, 0, 5]
    N = len(arr)
    print(findMinMoves(arr, N))
