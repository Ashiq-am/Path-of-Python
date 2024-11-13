# Python code for the above approach
def lower_bound(a, val):
    lo = 0
    hi = len(a) - 1
    while (lo < hi):
        mid = (lo + (hi - lo) // 2)
        if (a[mid] < val):
            lo = mid + 1
        else:
            hi = mid
    return lo


# Function to find the
# maximum number of elements
def maxNumbers(stack1, N, stack2, M, K):
    # Take prefix of both the stack
    sumA = [0] * (N + 1)
    sumB = [0] * (M + 1)
    for i in range(N):
        sumA[i + 1] = sumA[i] + stack1[i]

    for i in range(M):
        sumB[i + 1] = sumB[i] + stack2[i]

    # Calculate maxNumbers
    MaxNumbers = 0
    for i in range(N + 1):

        # Calculate remaining value of K
        # after selecting numbers
        # from 1st stack
        remValueOfK = K - sumA[i]

        # If rem value of K is less than 0
        # continue the loop
        if (remValueOfK < 0):
            continue

        # Calculate lower bound
        lowerBound = lower_bound(sumB, remValueOfK)

        # If size of lower bound is greater
        # than self stack size or
        # value of lower bound element
        # decrement lowerBound
        if (lowerBound > M or sumB[lowerBound] > remValueOfK):
            lowerBound -= 1

        # Store max possible numbers
        books = i + lowerBound
        MaxNumbers = max(MaxNumbers, books)

    return MaxNumbers


# Driver code

stack1 = [60, 90, 120]
stack2 = [100, 10, 10, 200]
K = 130
N = 3
M = 4
ans = maxNumbers(stack1, N, stack2, M, K)
print(ans)


