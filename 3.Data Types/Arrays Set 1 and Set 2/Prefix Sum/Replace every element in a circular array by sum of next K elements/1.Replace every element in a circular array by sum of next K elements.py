# Python3 program for
# the above approach

# Function to find the sum of next
# or previous k array elements
def sumOfKelementsUtil(a, x):
    # Size of the array
    n = len(a)

    # Stores the result
    ans = []

    # Iterate the given array
    for i in range(n):
        count = 0
        k = i + 1
        temp = 0

        # Traverse the k elements
        while (count < x):
            temp += a[k % n]
            count += 1
            k += 1

        # Push the K elements sum
        ans.append(temp)

    # Return the resultant vector
    return ans


# Function that prints the
# sum of next K element for
# each index in the array
def sumOfKelements(arr, K):
    # Size of the array
    N = len(arr)

    # Stores the result
    ans = []

    # If key is negative,
    # reverse the array
    if (K < 0):
        K = K * (-1)

        # Reverse the array
        arr = arr.reverse()

        # Find the resultant vector
        ans = sumOfKelementsUtil(arr, K)

        # Reverse the array again to
        # get the original sequence
        ans = ans.reverse()

    # If K is positive
    else:
        ans = sumOfKelementsUtil(arr, K)

    # Print the answer
    for i in range(N):
        print(ans[i], end=" ")


# Driver Code
if __name__ == "__main__":
    # Given array arr[]
    arr = [4, 2, -5, 11]
    K = 3

    # Function Calll
    sumOfKelements(arr, K)
