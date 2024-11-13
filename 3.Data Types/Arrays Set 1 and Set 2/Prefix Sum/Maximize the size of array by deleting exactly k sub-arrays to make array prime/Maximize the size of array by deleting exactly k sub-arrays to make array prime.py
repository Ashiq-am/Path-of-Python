# Python implementation of above approach

N = 10000005
prime = [False] * N


# Sieve of Eratosthenes
def seive():
    for i in range(2, N):
        if not prime[i]:
            for j in range(i + 1, N):
                prime[j] = True

    prime[1] = True


# Function to return the size
# of the maximized array
def maxSizeArr(arr, n, k):
    v, diff = [], []

    # Insert the indices of composite numbers
    for i in range(n):
        if prime[arr[i]]:
            v.append(i)

    # Compute the number of prime between
    # two consecutive composite
    for i in range(1, len(v)):
        diff.append(v[i] - v[i - 1] - 1)

    # Sort the diff vector
    diff.sort()

    # Compute the prefix sum of diff vector
    for i in range(1, len(diff)):
        diff[i] += diff[i - 1]

    # Impossible case
    if k > n or (k == 0 and len(v)):
        return -1

    # Delete sub-arrays of length 1
    elif len(v) <= k:
        return (n - k)

    # Find the number of primes to be deleted
    # when deleting the sub-arrays
    elif len(v) > k:
        tt = len(v) - k
        s = 0
        s += diff[tt - 1]
        res = n - (len(v) + s)
        return res


# Driver code
if __name__ == "__main__":
    seive()

    arr = [2, 4, 2, 2, 4, 2, 4, 2]
    n = len(arr)
    k = 2

    print(maxSizeArr(arr, n, k))


