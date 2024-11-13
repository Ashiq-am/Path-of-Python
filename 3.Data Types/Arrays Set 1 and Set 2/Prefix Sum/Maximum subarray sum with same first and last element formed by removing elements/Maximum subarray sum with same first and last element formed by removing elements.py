# Python3 program for the above approach
import sys


# Function to find the maximum sum
# of sub-array
def maximumSubarraySum(arr):
    # Initialize the variables
    N = len(arr);
    memo = {};
    res = -(sys.maxsize - 1);
    currsum = 0;
    currval = 0;

    # Traverse over the range
    for i in range(N):

        # Add the current value to the
        # variable currsum for prefix sum
        currval = arr[i];
        currsum = currsum + currval;

        # Calculate the result
        if currval in memo:

            if (currval > 0):
                res = max(res, currsum - memo[currval] + currval);
            else:
                res = max(res, currsum - memo[currval] + 2 * currval);

        else:
            memo[currval] = currsum;

        if (currval < 0):
            currsum = currsum - currval;

    # Return the answer
    return res;


# Driver Code
if __name__ == "__main__":
    arr = [-1, -3, 4, 0, -1, -2];
    print(maximumSubarraySum(arr));

# This code is contributed by AnkThon
