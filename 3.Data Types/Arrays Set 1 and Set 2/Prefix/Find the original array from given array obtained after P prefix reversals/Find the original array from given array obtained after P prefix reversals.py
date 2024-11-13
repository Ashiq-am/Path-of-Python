# Python program for the above approach
def find_original_array(arr, n, p):
    # Initialize the r and l
    r = p - 1;
    l = 0;

    # Initialize index = 0
    # to track elements at
    # odd and even positions
    index = 0;
    res = []

    while (l <= r):

        # If index is even
        if (index % 2 == 0):
            res.append(arr[l]);
            l += 1;

        # If index is odd
        else:
            res.append(arr[r]);
            r -= 1;

        # Increment index
        index = index + 1;

    # Reverse the res
    res.reverse();

    # Assign the modified prefix to arr
    for i in range(len(res)):
        arr[i] = res[i];

    # Print array arr
    # which is the original array
    # modified from the
    # prefix reversed array
    for i in range(n):
        print(arr[i], end=" ");


# Driver code
if __name__ == '__main__':
    arr = [4, 2, 1, 3, 5, 6]
    P = 4;
    n = len(arr);

    # Function call
    find_original_array(arr, n, P);

# This code is contributed by gauravrajput1
