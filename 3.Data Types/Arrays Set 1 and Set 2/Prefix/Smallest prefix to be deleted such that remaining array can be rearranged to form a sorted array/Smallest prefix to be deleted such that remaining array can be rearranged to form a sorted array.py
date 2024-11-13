# Python3 program for above approach

# Function to find the minimum length
# of prefix required to be deleted
def findMinLength(arr):
    # Stores index to be returned
    index = len(arr) - 1;

    # Iterate until previous element
    # is <= current index
    while (index > 0 and arr[index] >= arr[index - 1]):
        # Decrementing index
        index -= 1;

    # Return index
    return index;


# Driver code
if __name__ == '__main__':
    # Given arr
    arr = [7, 8, 5, 0, -1,
           -1, 0, 1, 2, 3, 4];
    n = len(arr);

    # Function call
    print(findMinLength(arr));

# This code is contributed by Princi Singh
