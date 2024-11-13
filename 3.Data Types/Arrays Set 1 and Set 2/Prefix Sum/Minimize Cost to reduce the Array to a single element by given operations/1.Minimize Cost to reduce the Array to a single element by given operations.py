# Python3 Program to implement
# the above approach
inf = 10000009


# Function to minimize the cost to
# reduce the array to a single element
def minCost(a, i, j, k):
    if (i >= j):
        # Base case
        # If n = 1 or n = 0
        return 0

    # Intialize cost to maximum value
    best_cost = inf

    # Iterate through all possible indices
    # and find the best index
    # to combine the subproblems
    for pos in range(i, j):
        # Compute left subproblem
        left = minCost(a, i, pos, k)

        # Compute right subproblem
        right = minCost(a, pos + 1, j, k)

        # Calculate the best cost
        best_cost = min(best_cost,
                        left + right +
                        k * Combine(a, i, j))

    # Return the answer
    return best_cost


# Function to combine
# the sum of the two halves
def Combine(a, i, j):
    sum = 0

    # Calculate the sum from i to j
    for l in range(i, j + 1):
        sum += a[l]

    return sum


# Driver code
if __name__ == '__main__':
    n = 4
    a = [4, 5, 6, 7]
    k = 3

    print(minCost(a, 0, n - 1, k))

