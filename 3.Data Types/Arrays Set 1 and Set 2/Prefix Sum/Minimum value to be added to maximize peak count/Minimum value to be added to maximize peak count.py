# Python3 code to implement above approach
import sys


# Function to find the minimum additional value
def good_elements(arr, n):
    ans = sys.maxsize;

    if (n % 2 == 1):
        ans = 0;

        # If the length is odd
        for i in range(1, n, 2):
            temp = max(arr[i + 1], arr[i - 1]) - arr[i] + 1;
            ans = ans + max(0, temp);

    else:

        # If the length is even
        pref = [0] * (n + 1);
        suff = [0] * (n + 1);

        for i in range(1, n - 1, 2):
            # Calculating the prefix sum excluding first
            # and last element
            temp = max(0, max(arr[i + 1], arr[i - 1]) - arr[i] + 1);
            pref[i + 1] = pref[i - 1] + temp;

        for i in range(n - 2, 1, -1):
            # Calculating the suffix sum excluding first
            # and last element
            temp = max(0, max(arr[i + 1], arr[i - 1]) - arr[i] + 1);
            suff[i - 1] = suff[i + 1] + temp;

        # Calculating ans for every configuration and
        # finding the minimum from those
        for i in range(0, n, 2):
            ans = min(ans, pref[i] + suff[i + 1]);

    return ans;


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 1, 1];
    N = len(arr);

    # Function call
    ans = good_elements(arr, N);
    print(ans);
