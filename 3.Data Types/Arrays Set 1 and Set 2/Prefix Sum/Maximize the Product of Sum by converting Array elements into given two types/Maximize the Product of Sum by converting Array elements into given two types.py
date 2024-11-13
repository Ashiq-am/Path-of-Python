# Python code to implement the approach

# Function to obtain maximum product
# along with sum of X and Y
def Max_Product(n, arr, Z):
    # Variable to store maximum product
    product = -10000000000000000000000

    # Sorting arr[]
    arr.sort()

    # Variabale to Hold sum of first type
    sum1 = 0

    # Variale to hold Maximum value
    # of first type sum
    X = -10000000000000000000000

    # Variale to hold Maximum value
    # of second type sum
    Y = 100000000000000000000000

    # Loop for iterating on sorted arr[]
    # from right to left for decreasing order
    for i in range(n - 1, 0, -1):
        sum1 += arr[i]
        sum2 = 0
        for j in range(i - 1, -1, -1):
            sum2 = sum2 + (Z - arr[j])
            if (sum1 * sum2 > product):
                product = sum1 * sum2
                X = sum1
                Y = sum2

    return product


# Driver code
if __name__ == "__main__":
    arr = [500, 100, 400, 560, 876]
    N = len(arr)
    Z = 1000

    # Function call
    print(Max_Product(N, arr, Z))

# This code is contributed by Rohit Pradhan
