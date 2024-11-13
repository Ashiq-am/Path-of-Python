# Python3 program to implement
# the above approach

# Function to find minimum number
# of elements required to form A[]
# by performing mirroring operation
def minimumrequired(A, N):
    # Initialize K
    K = N

    while (K > 0):

        # Odd length array
        # cannot be formed by
        # mirror operation
        if (K % 2) == 1:
            ans = K
            break

        ispalindrome = 1

        # Check if prefix of
        # length K is palindrome
        for i in range(0, K // 2):

            # Check if not a palindrome
            if (A[i] != A[K - 1 - i]):
                ispalindrome = 0

        # If found to be palindrome
        if (ispalindrome == 1):
            ans = K // 2
            K = K // 2

        # Otherwise
        else:
            ans = K
            break

    # Return the final answer
    return ans


# Driver code
A = [1, 2, 2, 1, 1, 2, 2, 1]
N = len(A)

print(minimumrequired(A, N))

# This code is contributed by VirusBuddah_
