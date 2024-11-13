# Python3 implementation to find
# elements that are a power of two
MAX = 10000

# prefix[i] is going to store the
# number of elements which are a
# power of two till i (including i).
prefix = [0] * (MAX + 1)


def isPowerOfTwo(x):
    if (x and (not (x & (x - 1)))):
        return True
    return False


# Function to find the maximum range
# whose sum is divisible by M.
def computePrefix(n, a):
    # Calculate the prefix sum
    if (isPowerOfTwo(a[0])):
        prefix[0] = 1

    for i in range(1, n):
        prefix[i] = prefix[i - 1]

        if (isPowerOfTwo(a[i])):
            prefix[i] += 1


# Function to return the number of elements
# which are a power of two in a subarray
def query(L, R):
    return prefix[R] - prefix[L - 1]


# Driver code
if __name__ == "__main__":
    A = [3, 8, 5, 2, 5, 10]
    N = len(A)
    Q = 2

    computePrefix(N, A)
    print(query(0, 4))
    print(query(3, 5))
