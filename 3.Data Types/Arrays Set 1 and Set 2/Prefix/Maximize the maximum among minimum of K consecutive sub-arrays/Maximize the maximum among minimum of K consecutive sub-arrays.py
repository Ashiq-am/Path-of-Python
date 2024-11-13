# Python3 implementation of the above approach
import sys


# Function to return maximum possible value
# of maximum of minimum of K sub-arrays
def maximizeMinimumOfKSubarrays(arr, n, k):
    m = sys.maxsize;
    M = -(sys.maxsize - 1);

    # Compute maximum and minimum
    # of the array
    for i in range(n):
        m = min(m, arr[i]);
        M = max(M, arr[i]);

    # If k = 1 then return the
    # minimum of the array
    if (k == 1):
        return m;

    # If k >= 3 then return the
    # maximum of the array
    elif (k >= 3):
        return M;

    # If k = 2 then maintain prefix
    # and suffix minimums
    else:

        # Arrays to store prefix
        # and suffix minimums
        L = [0] * n;
        R = [0] * n;

        L[0] = arr[0];
        R[n - 1] = arr[n - 1];

        # Prefix minimum
        for i in range(1, n):
            L[i] = min(L[i - 1], arr[i]);

        # Suffix minimum
        for i in range(n - 2, -1, -1):
            R[i] = min(R[i + 1], arr[i]);

        maxVal = -(sys.maxsize - 1);

        # Get the maximum possible value
        for i in range(n - 1):
            maxVal = max(maxVal, max(L[i],
                                     R[i + 1]));

        return maxVal;


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5];
    n = len(arr);
    k = 2;

    print(maximizeMinimumOfKSubarrays(arr, n, k));

# This code is contributed by Ryuga
