# Python 3 program to find the index with
# minimum sum of prefix and suffix
# sums in an Array

def indexMinSum(arr, n):
    # Initialization of the min value
    min = arr[0]
    index = 0

    # Find minimum element in the array
    for i in range(1, n):
        if (arr[i] < min):
            # store the index of the
            # current minimum element
            min = arr[i]
            index = i

        # return the index of min element
    # 1-based index
    return index + 1


# Driver Code
if __name__ == "__main__":
    arr = [6, 8, 2, 3, 5]
    n = len(arr)
    print(indexMinSum(arr, n))

