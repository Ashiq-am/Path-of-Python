# Python code for the above approach

# Function to find the minimum count
# of required insertions
def getElements(N, arr):
    # To store the previous sums
    forSum = {}

    # Final answer
    ans = 0

    # To store current sum
    sum = 0

    # Traversing array
    for i in range(N):

        # Adding elements
        sum += arr[i]

        # Storing occurence
        if (sum in forSum):
            forSum[sum] += 1
        else:
            forSum[sum] = 1

        # If found any subarray with sum 0
        if (sum == 0 or forSum[sum] > 1):
            ans += 1

            # New sum
            sum = arr[i]

            # Clearing previous data
            forSum.clear()

            # Storing new sum
            if (sum in forSum):
                forSum[sum] += 1
            else:
                forSum[sum] = 1

    return ans


# Driver Code
N = 3
arr = [1, -1, 1]

# Function call
print(getElements(N, arr))

