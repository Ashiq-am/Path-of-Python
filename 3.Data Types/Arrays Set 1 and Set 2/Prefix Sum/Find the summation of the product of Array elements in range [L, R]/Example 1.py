# Python program for the above approach:

## Function to return the sum
## of (arr[i]*arr[j]) for all i and j
## between the index L and R
def sum_of_products(arr, N, L, R):
    sum1 = 0

    for i in range(L, R + 1):
        for j in range(i, R + 1):
            sum1 += arr[i] * arr[j]
    return sum1


## Driver code
if __name__ == "__main__":
    arr = [1, 3, 5, 8]
    N = len(arr)
    L = 0
    R = 2
    print(sum_of_products(arr, N, L, R))

# This code is contributed by entertain2022.
