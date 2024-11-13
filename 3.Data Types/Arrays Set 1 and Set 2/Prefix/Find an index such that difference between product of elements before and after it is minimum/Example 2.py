import math


# Function to find index
def solve(Array, N):
    # Array to store log values of elements
    Arraynew = [0] * N
    for i in range(N):
        Arraynew[i] = math.log(Array[i])

    # Prefix Array to Maintain Sum of log values till index i
    prefixsum = [0] * N
    prefixsum[0] = Arraynew[0]

    for i in range(1, N):
        prefixsum[i] = prefixsum[i - 1] + Arraynew[i]

    # Answer Index
    answer = 0
    minabs = abs(prefixsum[N - 1] - 2 * prefixsum[0])

    for i in range(1, N - 1):
        ans1 = abs(prefixsum[N - 1] - 2 * prefixsum[i])

        # Find minimum absolute value
        if (ans1 < minabs):
            minabs = ans1
            answer = i

    print("Index is: ", answer)


# Driver Code
if __name__ == "__main__":
    Array = [1, 4, 12, 2, 6]
    N = 5
    solve(Array, N)

# This code is contributed by chitranayal
