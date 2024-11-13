# Python 3 program to divide into
# maximum number of segments
import sys


# Returns the maximum number of sorted
# subarrays in a valid partition
def sorted_partitions(arr, n):
    right_min = [0] * (n + 1)
    right_min[n] = sys.maxsize
    for i in range(n - 1, -1, -1):
        right_min[i] = min(right_min[i + 1], arr[i])

    # Finding the shortest prefix such that
    # all the elements in the prefix are less
    # than or equal to the elements in the
    # rest of the array.
    partitions = 0
    current_max = arr[0]
    for i in range(n):
        current_max = max(current_max, arr[i])

        # if current max is less than the right
        # prefix min, we increase number of partitions.
        if (current_max <= right_min[i + 1]):
            partitions += 1

    return partitions


# Driver code
arr = [3, 1, 2, 4, 100, 7, 9]

# Find minimum value from right
# for every index
n = len(arr)
ans = sorted_partitions(arr, n)
print(ans)
