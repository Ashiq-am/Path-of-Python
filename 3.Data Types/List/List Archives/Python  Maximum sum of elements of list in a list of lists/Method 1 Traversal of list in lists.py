# Python program to find the
# list in a list of lists whose
# sum of elements is the highest
# using traversal

def maximumSum(list1):
    maxi = 0

    # traversal in the lists
    for x in list1:
        sum = 0
        # traversal in list of lists
        for y in x:
            sum += y
        maxi = max(sum, maxi)

    return maxi


# driver code
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))
