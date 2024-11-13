# Python3 program for the above approach

# Function to count maximum number
# of non-overlapping subarrays with
# sum equals to the target
def maximumSubarrays(arr, N, target):
    # Stores the final count
    ans = 0

    # Next subarray should start
    # from index >= availIdx
    availIdx = -1

    # Tracks the prefix sum
    cur_sum = 0

    # Map to store the prefix sum
    # for respective indices
    mp = {}
    mp[0] = -1

    for i in range(N):
        cur_sum += arr[i]

        # Check if cur_sum - target is
        # present in the array or not
        if ((cur_sum - target) in mp and
                mp[cur_sum - target] >= availIdx):
            ans += 1
            availIdx = i

        # Update the index of
        # current prefix sum
        mp[cur_sum] = i

    # Return the count of subarrays
    return ans


# Driver Code
if __name__ == '__main__':
    # Given array arr[]
    arr = [2, -1, 4, 3,
           6, 4, 5, 1]

    N = len(arr)

    # Given sum target
    target = 6

    # Function call
    print(maximumSubarrays(arr, N, target))


