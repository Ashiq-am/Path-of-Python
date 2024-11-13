# Python code to break out of multiple
# loops by using an else block


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

        # If the inner loop completes without encountering
        # the break statement then the following else
        # block will be executed and outer loop will
        # continue to the next value of i:
        else:
            continue

        # If the inner loop terminates due to the
        # break statement, the else block will not
        # be executed and the following break
        # statement will terminate the outer loop also:
        break


# Driver Code:
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 4
elementInArray(arr, x)
