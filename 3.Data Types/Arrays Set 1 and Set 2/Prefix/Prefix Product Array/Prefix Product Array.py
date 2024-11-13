# Python3 Program to generate
# Prefix Product Array

# Function to generate
# prefix product array
def prefixProduct(a, n):
    # Update the array
    # with the product of
    # prefixes
    for i in range(1, n):
        a[i] = a[i] * a[i - 1];

    # Print the array
    for j in range(0, n):
        print(a[j], end=", ");

    return 0;


# Driver Code
arr = [2, 4, 6, 5, 10];
N = len(arr);
prefixProduct(arr, N);

# This code is contributed by Code_Mech
