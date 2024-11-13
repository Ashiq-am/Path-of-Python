# Python3 program to check
# if all array elements are
# same or not.
def areSame(arr):
    first = arr[0]

    for i in range(1, len(arr)):
        if (arr[i] != first):
            return False

    return True


# Driver code
if __name__ == '__main__':

    arr = [1, 2, 3, 2]

    if (areSame(arr)):
        print("All Elements are Same")
    else:
        print("Not all Elements are Same")

