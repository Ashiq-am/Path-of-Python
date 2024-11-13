# Python program to find Maximum product
# of elements of list in a list of lists


def prod(lis):
    maxi = 0

    # traversal in the lists
    for x in lis:

        p = 1

        # traversal in list of lists
        for i in x:
            p *= i
            maxi = max(p, maxi)
    return maxi


# driver code
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(prod(l))
