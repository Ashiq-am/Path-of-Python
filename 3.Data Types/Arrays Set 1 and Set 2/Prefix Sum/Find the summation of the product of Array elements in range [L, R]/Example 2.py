# Python program for the above approach:

## Function to return the sum of
## (arr[i]*arr[j]) for all i and j
## between the index L and R
def sum_of_products(arr, n, L, R):
    sum = 0
    ## Pre-calculating Prefix sum
    prefix_sum = [0] * n;
    prefix_sum[0] = arr[0];
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    ## Using prefix sum to find
    ## summation of products
    for i in range(L, R + 1):

        ## if-else for i==0 case
        ## in prefix sum
        if (i != 0):
            sum += arr[i] * (prefix_sum[R] - prefix_sum[i - 1])
        else:
            sum += arr[i] * (prefix_sum[R])

    return sum


## Driver code
if __name__ == '__main__':
    arr = [1, 3, 5, 8]
    N = len(arr)
    L = 0
    R = 2
    print(sum_of_products(arr, N, L, R))

# This code is contributed by subhamgoyal2014.
