# Pyhton3 program to implement
# the above approach

# Function to print the cost
# to move all 1s to each index
def costMove1s(arr, N):
    # Traverse the array.
    for i in range(0, N):

        # Stores cost to move
        # all 1s at current index
        cost = 0

        # Calculate cost to move
        # all 1s at current index
        for j in range(0, N):

            # If current element
            # of the array is 1.
            if (arr[j] == 1):
                # Update cost
                cost = cost + abs(i - j)

        print(cost, end=" ")


# Driver Code
if __name__ == "__main__":
    arr = [0, 1, 0, 1]
    N = len(arr)

    costMove1s(arr, N)
