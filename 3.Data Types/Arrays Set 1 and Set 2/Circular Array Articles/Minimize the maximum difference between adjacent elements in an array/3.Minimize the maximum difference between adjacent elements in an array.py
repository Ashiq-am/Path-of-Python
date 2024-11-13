# Python3 implementation to find the
# minimum of the maximum difference
# of the adjacent elements after
# removing K elements from the array
import sys


# Function to find the minimum
# different in the subarrays
# of size K in the array
def findKMin(arr, n, k):
    # Create a Double Ended Queue, Qi
    # that will store indexes
    # of array elements, queue will
    # store indexes of useful elements
    # in every window
    Qi = []

    # Process first k (or first window)
    # elements of array
    i = 0

    for j in range(k):

        # For every element,
        # the previous smaller elements
        # are useless so remove them from Qi
        while ((len(Qi) != 0) and
               arr[i] >= arr[Qi[-1]]):
            Qi.pop()  # Remove from rear

        # Add new element at rear of queue
        Qi.append(i)
        i += 1

    minDiff = sys.maxsize

    # Process rest of the elements,
    # i.e., from arr[k] to arr[n-1]
    for j in range(i, n):

        # The element at the front
        # of the queue is the largest
        # element of previous window
        minDiff = min(minDiff, arr[Qi[0]])

        # Remove the elements
        # which are out of this window
        while ((len(Qi) != 0) and
               Qi[0] <= i - k):
            Qi.pop(0)

        # Remove all elements smaller
        # than the currently being
        # added element (remove
        # useless elements)
        while ((len(Qi) != 0) and
               arr[i] >= arr[Qi[-1]]):
            Qi.pop()

        # Add current element
        # at the rear of Qi
        Qi.append(i)
        i += 1

    # Compare the maximum
    # element of last window
    minDiff = min(minDiff, arr[Qi[0]])

    return minDiff


# Function to find the minimum
# of the maximum difference of the
# adjacent elements after removing
# K elements from the array
def minimumAdjacentDifference(a, n, k):
    # Create the difference array
    diff = [0 for i in range(n - 1)]

    for i in range(n - 1):
        diff[i] = a[i + 1] - a[i]

    # Find minimum of all maximum
    # of subarray sizes n - k - 1
    answer = findKMin(diff, n - 1,
                      n - k - 1)
    return answer


# Driver code
if __name__ == "__main__":
    n = 5
    k = 2

    a = [3, 7, 8, 10, 14]

    print(minimumAdjacentDifference(a, n, k))
