# Python3 program for
# the above approach
arr = [10, 2, -2, -20, 10]
n = len(arr)
k = -10
res = 0

# Calculate all subarrays
for i in range(n):
    summ = 0
    for j in range(i, n):

        # Calculate required sum
        summ += arr[j]

        # Check if sum is equal to
        # required sum
        if summ == k:
            res += 1

print(res)

