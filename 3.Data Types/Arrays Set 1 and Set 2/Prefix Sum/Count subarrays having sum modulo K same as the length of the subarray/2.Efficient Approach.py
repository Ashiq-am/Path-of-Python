# Python3 program of the above approach

# Function that counts the subarrays
# s.t. sum of elements in the subarray
# modulo k is equal to size of subarray
def countSubarrays(a, n, k):
    # Stores the count of (pref[i] - i) % k
    cnt = {}

    # Stores the count of subarray
    ans = 0

    # Stores prefix sum of the array
    pref = []
    pref.append(0)

    # Find prefix sum array
    for i in range(n):
        pref.append((a[i] + pref[i]) % k)

    # Base Condition
    cnt[0] = 1

    for i in range(1, n + 1):

        # Remove the index at present
        # after K indices from the
        # current index
        remIdx = i - k

        if (remIdx >= 0):
            if ((pref[remIdx] -
                 remIdx % k + k) % k in cnt):
                cnt[(pref[remIdx] -
                     remIdx % k + k) % k] -= 1
            else:
                cnt[(pref[remIdx] -
                     remIdx % k + k) % k] = -1

        # Update the answer for subarrays
        # ending at the i-th index
        if (pref[i] - i % k + k) % k in cnt:
            ans += cnt[(pref[i] - i % k + k) % k]

        # Add the calculated value of
        # current index to count
        if (pref[i] - i % k + k) % k in cnt:
            cnt[(pref[i] - i % k + k) % k] += 1
        else:
            cnt[(pref[i] - i % k + k) % k] = 1

    # Print the count of subarrays
    print(ans, end=' ')


# Driver code

# Given arr[]
arr = [2, 3, 5, 3, 1, 5]

# Size of the array
N = len(arr)

# Given K
K = 4

# Function call
countSubarrays(arr, N, K)

