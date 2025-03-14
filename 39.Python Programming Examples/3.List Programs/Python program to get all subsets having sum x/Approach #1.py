# Python code with time complexity
# O(2^n)to print all subsets whose
# sum is equal to a given value
from itertools import combinations


def subsetSum(n, arr, x):
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    for i in range(n + 1):
        for subset in combinations(arr, i):

            # printing the subset if its sum is x:
            if sum(subset) == x:
                print(list(subset))


# Driver Code:
n = 6
arr = [10, 20, 25, 50, 70, 90]
x = 80
subsetSum(n, arr, x)
