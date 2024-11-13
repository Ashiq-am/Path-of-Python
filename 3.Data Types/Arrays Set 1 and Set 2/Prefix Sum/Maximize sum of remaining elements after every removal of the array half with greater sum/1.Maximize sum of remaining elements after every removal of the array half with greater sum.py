# Python3 program to implement
# the above approach

# Function to find the maximum sum
def maxweight(s, e, pre):
    # Base case
    # len of array is 1
    if s == e:
        return 0

    # Stores the final result
    ans = 0

    # Traverse the array
    for i in range(s, e):

        # Store left prefix sum
        left = pre[i] - pre[s - 1]

        # Store right prefix sum
        right = pre[e] - pre[i]

        # Compare the left and right
        if left < right:
            ans = max(ans, left \
                      + maxweight(s, i, pre))

        # If both are equal apply
        # the optimal method
        if left == right:
            # Update with minimum
            ans = max(ans, left \
                      + maxweight(s, i, pre),
                      right \
                      + maxweight(i + 1, e, pre))

        if left > right:
            ans = max(ans, right \
                      + maxweight(i + 1, e, pre))

    # Return the final ans
    return ans


# Function to print maximum sum
def maxSum(arr):
    # Dicitionary to store prefix sums
    pre = {-1: 0, 0: arr[0]}

    # Traversing the array
    for i in range(1, len(arr)):
        # Add prefix sum of the array
        pre[i] = pre[i - 1] + arr[i]

    print(maxweight(0, len(arr) - 1, pre))


# Drivers Code

arr = [6, 2, 3, 4, 5, 5]

# Function Call
maxSum(arr)
