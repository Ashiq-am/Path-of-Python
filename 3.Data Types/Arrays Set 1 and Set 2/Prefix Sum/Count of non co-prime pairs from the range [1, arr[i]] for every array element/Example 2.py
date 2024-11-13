MAX = 1005;


def preCalculate(phi, ans):
    phi[0] = 0
    phi[1] = 1

    # Iterate over the range [1, MAX]
    for i in range(2, MAX + 1):
        phi[i] = i

    # Iterate over the range [1, MAX]
    for i in range(2, MAX + 1):
        if (phi[i] == i):
            for j in range(i, MAX + 1, i):
                # Subtract the number of
                # pairs which has i as one
                # of their factors
                phi[j] -= (phi[j] // i);

    # Iterate over the range [1, MAX]
    for i in range(1, MAX + 1):
        ans[i] = ans[i - 1] + (i - phi[i]);


# Function to count the number of
# non co-prime pairs for each query
def countPairs(arr, N):
    # The i-th element stores
    # the count of element that
    # are co-prime with i
    phi = [0 for i in range(100001)]

    # Stores the resulting array
    ans = [0 for i in range(100001)]

    # Function Call
    preCalculate(phi, ans);

    # Traverse the array arr[]
    for i in range(N):
        print(ans[arr[i]], end=' ');


# Given Input
arr = [5, 10, 20]
N = 3;

# Function Call
countPairs(arr, N);

# This code is contributed by rutvik_56.
