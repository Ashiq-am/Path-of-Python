# Python3 program to find subarray
# with sum closest to 0
class prefix:

    def __init__(self, sum, index):
        self.sum = sum
        self.index = index

    # Returns subarray with sum closest to 0.


def findSubArray(arr, n):
    start, end, min_diff = None, None, float('inf')

    pre_sum = [None] * (n + 1)

    # To consider the case of subarray
    # starting from beginning of the array
    pre_sum[0] = prefix(0, -1)

    # Store prefix sum with index
    for i in range(1, n + 1):
        pre_sum[i] = prefix(pre_sum[i - 1].sum +
                            arr[i - 1], i - 1)

    # Sort on the basis of sum
    pre_sum.sort(key=lambda x: x.sum)

    # Find two consecutive elements
    # with minimum difference
    for i in range(1, n + 1):
        diff = pre_sum[i].sum - pre_sum[i - 1].sum

        # Update minimum difference
        # and starting and ending indexes
        if min_diff > diff:
            min_diff = diff
            start = pre_sum[i - 1].index
            end = pre_sum[i].index

        # Return starting and ending indexes
    return (start + 1, end)


# Driver code
if __name__ == "__main__":
    arr = [2, 3, -4, -1, 6]
    n = len(arr)

    point = findSubArray(arr, n)
    print("Subarray starting from",
          point[0], "to", point[1])


