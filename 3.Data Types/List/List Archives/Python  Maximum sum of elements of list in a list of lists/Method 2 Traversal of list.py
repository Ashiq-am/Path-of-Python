# Python program to find the
# list in a list of lists whose
# sum of elements is the highest
# using sum and max function and traversal

def maximumSum(list1):
    maxi = 0
    # traversal
    for x in list1:
        maxi = max(sum(x), maxi)

    return maxi


# driver code
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))
