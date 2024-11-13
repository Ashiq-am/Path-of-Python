# Python3 program for the above approach
MAX = 100005


# Function to return all prime numbers
# smaller than N
def SieveOfEratosthenes():
    # Create a boolean array "prime[0..n]"
    seive = [True for i in range(MAX)]

    # Initialize all its entries as true
    # memset(seive, true, sizeof(seive))
    for p in range(2, MAX):
        if p * p > MAX:
            break

        # If prime[p] is not changed,
        # then it is a prime
        if (seive[p] == True):

            # Update all multiples of
            # p greater than or equal
            # to the square of it
            for i in range(p * p, MAX, p):
                seive[i] = False

    # Stores all prime numbers
    # smaller than MAX
    v = []

    # Store all prime numbers
    for p in range(2, MAX):

        # If p is prime
        if (seive[p]):
            v.append(p)

    return v


# Function to build the auxiliary DP
# array from the start
def build(dp, arr, N):
    # Base Case
    dp[0] = 0
    dp[1] = 0

    # Stores all prime numbers < N
    prime = SieveOfEratosthenes()

    # Stores prefix sum
    pref = [0 for i in range(N + 1)]
    pref[0] = 0

    # Update prefix sum
    for i in range(1, N + 1):
        pref[i] = pref[i - 1] + arr[i - 1]

    # Iterate over range
    for i in range(2, N + 1):

        # Update each state i.e.. when
        # current element is excluded
        dp[i] = dp[i - 1]

        for j in range(len(prime) + 1):

            # Find start & end index
            # of subarrays when prime[i]
            # is taken
            r = i - 1
            l = r - prime[j] + 1

            # Check if starting point
            # lies in the array
            if (l < 0):
                break

            temp = 0

            # Include the elements
            # al al+1 ... ar
            temp = pref[r + 1] - pref[l]

            # Check if element lies before
            # start of selected subarray
            if (l - 2 >= 0):
                temp += dp[l - 2 + 1]

            # Update value of dp[i]
            dp[i] = max(dp[i], temp)


# Function to find the maximum sum
# subsequence with prime length
def maxSumSubseq(arr, N):
    # Auxiliary DP array
    dp = [0 for i in range(N + 1)]

    # Build DP array
    build(dp, arr, N)

    # Print the result
    print(dp[N])


# Driver Code
if __name__ == '__main__':
    # Given arr[]
    arr = [10, 10, 7, 10, 10, 10]

    # Size of array
    N = len(arr)

    # Function Call
    maxSumSubseq(arr, N)
