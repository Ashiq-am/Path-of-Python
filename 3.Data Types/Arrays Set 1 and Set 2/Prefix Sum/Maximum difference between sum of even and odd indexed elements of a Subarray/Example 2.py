# Python code to implement the approach

# Function to get the sum of elements from i to j
def pre(arr, i, j):
    if(i == 0):
        return arr[j]
    return arr[j] - arr[i-1]

# Function to get the maximum possible difference
# between odd and even indexed elements of a subarray
def maximumDiff(nums):
    n = len(nums)
    val = 0
    odd = [0] * n
    even = [0] * n
    even[0] = nums[0]

    # Loop to create the odd[] and even[] array
    for i in range(1, n):
        if(i % 2 == 0):
            even[i] = nums[i]
        else:
            odd[i] = nums[i]
        odd[i] += odd[i-1]
        even[i] += even[i-1]

    # Loop to calculate the maximum possible
    # difference among all subarrays
    for i in range(n):
        for j in range(i, n):
            sum1 = pre(odd, i, j)
            sum2 = pre(even, i, j)
            val = max(val, abs(sum1 - sum2))

    # Return the maximum possible difference
    return val

nums = [1, 2, 3, 4, -5]
# Function call
ans = maximumDiff(nums)
print(ans)

# This code is contributed by lokesh.