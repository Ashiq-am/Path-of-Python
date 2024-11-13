# Python3 implementation of above approach
MAX = 10 ** 6 + 5
from math import ceil


# Function to find answer of each query
def query(arr, Q):
    # Stores the count of points with sum
    # less than or equal to their indices
    pre = [0] * (MAX)

    # Traverse the array
    for i in range(len(arr)):

        # ` If both x and y-coordinate < 0
        if (arr[i][0] < 0 or arr[i][1] < 0):
            continue

        # Stores the sum of co-ordinates
        sum = ceil((arr[i][0] + arr[i][1]));

        # Increment count of sum by 1
        pre[sum] += 1

    # Prefix array
    for i in range(1, MAX):
        pre[i] += pre[i - 1]

    # Perform queries
    for i in range(len(Q)):
        print(pre[Q[i]], end=" ")


# Drivers Code
if __name__ == '__main__':
    arr = [[2.1, 3.0],
           [3.7, 1.2],
           [1.5, 6.5],
           [1.2, 0.0]]
    Q = [2, 8, 5]
    N = len(arr)
    M = len(Q)

    query(arr, Q)
