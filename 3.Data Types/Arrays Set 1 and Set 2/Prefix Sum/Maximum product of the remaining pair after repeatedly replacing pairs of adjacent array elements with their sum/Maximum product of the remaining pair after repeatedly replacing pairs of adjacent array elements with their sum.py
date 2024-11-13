# Python program for the above approach
import sys


# Function to find the maximum product
# possible after repeatedly replacing
# pairs of adjacent array elements
# with their sum
def maxProduct(arr, N):
    # Store the maximum product
    max_product = -sys.maxsize;

    # Store the prefix sum
    prefix_sum = 0;

    # Store the total sum of array
    sum = 0;

    # Traverse the array to find
    # the total sum
    for i in range(N):
        sum += arr[i];

    # Iterate in the range [0, N-2]
    for i in range(N - 1):
        # Add arr[i] to prefix_sum
        prefix_sum += arr[i];

        # Store the value of prefix_sum
        X = prefix_sum;

        # Store the value of
        # (total sum - prefix sum)
        Y = sum - prefix_sum;

        # Update the maximum product
        max_product = max(max_product, X * Y);

    # Print the answer
    print(max_product);


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 5, 6, 7];
    N = len(arr);
    maxProduct(arr, N);

# This code is contributed by shikhasingrajput
