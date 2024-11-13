# Python program for the above approach

# Function to count the minimum number
# of pairs of adjacent elements required
# to be replaced by their sum to make all
# arrat elements equal
def minSteps(a, n):
    # Stores the prefix sum of the array
    prefix_sum = a[:]

    # Calculate the prefix sum array
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1]

    # Stores the maximum number of subarrays
    # into which the array can be split
    mx = -1

    # Iterate over all possible sums
    for subgroupsum in prefix_sum:

        sum = 0
        i = 0
        grp_count = 0

        # Traverse the array
        while i < n:
            sum += a[i]

            # If the sum is equal to
            # the current prefix sum
            if sum == subgroupsum:

                # Increment count
                # of groups by 1
                grp_count += 1
                sum = 0

            # Otherwise discard
            # this subgroup sum
            elif sum > subgroupsum:

                grp_count = -1
                break

            i += 1

        # Update the maximum
        # this of subarrays
        if grp_count > mx:
            mx = grp_count

        # Return the minimum
    # number of operations
    return n - mx


# Driver Code
if __name__ == '__main__':
    A = [1, 2, 3, 2, 1, 3]
    N = len(A)

    # Function Call
    print(minSteps(A, N))
