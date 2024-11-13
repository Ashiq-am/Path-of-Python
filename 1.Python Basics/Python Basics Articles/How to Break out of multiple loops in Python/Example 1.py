def elementInArray(arr, x):
    # Iterating through all
    # lists present in arr:
    for i in arr:

        # Iterating through all the elements
        # of each of the nested lists in arr:
        for j in i:

            # Checking if any element in the
            # nested list is equal to x:
            if j == x:
                print('Element found')
                break
            else:
                print(j)


# Driver Code:
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 4
elementInArray(arr, x)
