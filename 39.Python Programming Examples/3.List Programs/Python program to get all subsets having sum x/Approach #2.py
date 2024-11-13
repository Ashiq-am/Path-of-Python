# Efficient Python code to
# print all subsets whose sum
# is equal to a given value
from itertools import combinations


def subsetSum(li, comb, sums):
    # Iterating through all subsets of
    # list li from length 0 to length of li:
    for i in range(len(li) + 1):
        for subset in combinations(li, i):
            # Storing all the subsets in list comb:
            comb.append(list(subset))

            # Storing the subset sums in list sums:
            sums.append(sum(subset))


def calcSubsets(n, arr, x):
    # Dividing the list arr into two lists
    # arr1 and arr2 of about equal sizes
    # by slicing list arr about index n//2:
    arr1, arr2 = arr[:n // 2], arr[n // 2:]

    # Creating empty lists comb1 and sums1
    # to run the subsetSum function and
    # store subsets of arr1 in comb1
    # and the subset sums in sums1:
    comb1, sums1 = [], []
    subsetSum(arr1, comb1, sums1)

    # Creating empty lists comb2 and sums2
    # to run the subsetSum function and
    # store subsets of arr2 in comb2
    # and the subset sums in sums2:
    comb2, sums2 = [], []
    subsetSum(arr2, comb2, sums2)

    # Iterating i through the indices of sums1:
    for i in range(len(sums1)):

        # Iterating j through the indices of sums2:
        for j in range(len(sums2)):

            # If two elements (one from sums1
            # and one from sums2) add up to x,
            # the combined list of elements from
            # corresponding subsets at index i in comb1
            # and j in comb2 gives us the required answer:
            if sums1[i] + sums2[j] == x:
                print(comb1[i] + comb2[j])


# Driver Code:
n = 6
arr = [10, 20, 25, 50, 70, 90]
x = 80
calcSubsets(n, arr, x)
