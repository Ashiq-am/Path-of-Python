# Python program for the above approach
arr = [0] * 100005

# Function to check if the number x
# is divisible by its sum of digits
def isDivisible(x):
    # Stores sum of digits of x
    sum = 0;

    # Temporarily store x
    temp = x;

    # Calculate sum
    # of digits of x
    while (x != 0):
        sum += x % 10;
        x = x // 10;

    # If x is not divisible by sum
    if (temp % sum != 0):
        return False;

    # Otherwise
    else:
        return True;


# Function to perform
# the precomputation
def precompute():
    # Iterate from i equals 1 to 1e5
    for i in range(1, 100000 + 1):

        # Check if i is divisible
        # by sum of its digits
        if (isDivisible(i)):
            arr[i] = 1;

        else:
            arr[i] = 0;

    # Convert arr[] to prefix sum array
    for i in range(1, 100000 + 1):
        arr[i] = arr[i] + arr[i - 1];


# Driver Code

# Given queries
Q = [[5, 9], [5, 20]];

precompute();

for q in Q:
    # Using inclusion-exclusion
    # principle, calculate the result
    print(arr[q[1]] - arr[q[0] - 1]);

# This code is contributed by saurabh_jaiswal.
