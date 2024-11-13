# Python code to implement the approach

# dp array to store repeated state
dp = [[0 for i in range(100)] for j in range(100)]


# Function to find the maximum possible points
def maxPoint(i, j, arr, temp):
    # Base case
    if (i >= j):
        return 0
    if (j - i == 1):
        return 2 * min(arr[i], arr[j])
    if (dp[i][j] != -1):
        return dp[i][j]
    ans = 0
    for k in range(i, j):
        # Points rewarded for left subarray
        ans1 = maxPoint(i, k, arr, temp)

        # Points rewarded for right subarray
        ans2 = maxPoint(k + 1, j, arr, temp)
        left_element = temp[k + 1] - temp[i]
        right_element = temp[j + 1] - temp[k + 1]
        total = ans1 + ans2 + min(left_element, right_element) * 2

        # Total points for partition at current index
        ans = max(total, ans)

    # Store the ans in dp state and return the ans
    dp[i][j] = ans
    return dp[i][j]


def findMax(arr, N):
    temp = []
    temp.append(0)

    # To store sum of each elements
    s = 0
    for i in range(N):
        s = s + arr[i]
        temp.append(s)

    # Initializing DP array with -1
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            dp[i][j] = -1

    return maxPoint(0, N - 1, arr, temp)


# Driver Code
arr = [2, 3, 5]
N = len(arr)

# Function call
ans = findMax(arr, N)
print(ans)

# This code is contributed by Pushpesh Raj.
