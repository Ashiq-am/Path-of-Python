# Python3 program to implement
# the above approach

# Function to find the maximum sum
def maxweight(s, e, pre, dp):
    # Base Case
    if s == e:
        return 0

    # Create a key to map
    # the values
    key = (s, e)

    # Check if mapped key is
    # found in the dictionary
    if key in dp:
        return dp[key]

    ans = 0

    # Traverse the array
    for i in range(s, e):

        # Store left prefix sum
        left = pre[i] - pre[s - 1]

        # Store right prefix sum
        right = pre[e] - pre[i]

        # Compare the left and
        # right values
        if left < right:
            ans = max(ans, left \
                      + maxweight(s, i, pre, dp))

        if left == right:
            # Update with minimum
            ans = max(ans, left \
                      + maxweight(s, i, pre, dp),
                      right \
                      + maxweight(i + 1, e, pre, dp))

        if left > right:
            ans = max(ans, right \
                      + maxweight(i + 1, e, pre, dp))

        # Store the value in dp array
        dp[key] = ans

    # Return the final answer
    return dp[key]


# Function to print maximum sum
def maxSum(arr):
    # Stores prefix sum
    pre = {-1: 0, 0: arr[0]}

    # Store results of subproblems
    dp = {}

    # Traversing the array
    for i in range(1, len(arr)):
        # Add prefix sum of array
        pre[i] = pre[i - 1] + arr[i]

    # Print the answer
    print(maxweight(0, len(arr) - 1, pre, dp))


# Driver Code

arr = [6, 2, 3, 4, 5, 5]

# Function Call
maxSum(arr)
