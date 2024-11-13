# Python Implementation

def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)

def min_notes(N, A):
    sum = 0
    ans = 1000000000

    pref = [0] * N
    suff = [0] * N

    for i in range(N):
        sum += A[i]

    if N == 1:
        return 1


    pref[0] = A[0]
    for i in range(1, N):
        pref[i] = gcd(pref[i - 1], A[i])

    suff[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        suff[i] = gcd(suff[i + 1], A[i])


    for i in range(N):
        g = 0
        if i == 0:
            g = suff[i + 1]

        elif i == N - 1:
            g = pref[i - 1]

        else:
            g = gcd(pref[i - 1], suff[i + 1])

        val = (sum - A[i]) // g
        if val < ans:
            ans = val

    return ans + 1

N = 3

A = [2, 3, 4]

print(min_notes(N, A))
