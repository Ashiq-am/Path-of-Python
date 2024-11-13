# Python3 program for the above approach

# Function that counts the subarrays
# having sum modulo k equal to the
# length of subarray
def countSubarrays(a, n, k):
    # Stores the count
    # of subarrays
    ans = 0

    # Stores prefix sum
    # of the array
    pref = []
    pref.append(0)

    # Calculate prefix sum array
    for i in range(n):
        pref.append((a[i] + pref[i]) % k)

    # Generate all the subarrays
    for i in range(1, n + 1, 1):
        for j in range(i, n + 1, 1):

            # Check if this subarray is
            # a valid subarray or not
            if ((pref[j] -
                 pref[i - 1] + k) %
                    k == j - i + 1):
                ans += 1

    # Total count of subarrays
    print(ans, end=' ')


# Driver Code

# Given arr[]
arr = [2, 3, 5, 3, 1, 5]

# Size of the array
N = len(arr)

# Given K
K = 4

# Function call
countSubarrays(arr, N, K)
