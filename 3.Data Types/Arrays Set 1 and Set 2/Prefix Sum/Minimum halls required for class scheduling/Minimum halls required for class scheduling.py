# Python3 implementation of the approach
MAX = 100001


# Function to return the minimum
# number of halls required
def minHalls(lectures, n):
    # Array to store the number of
    # lectures ongoing at time t
    prefix_sum = [0] * MAX;

    # For every lecture increment start
    # point s decrement (end point + 1)
    for i in range(n):
        prefix_sum[lectures[i][0]] += 1;
        prefix_sum[lectures[i][1] + 1] -= 1;

    ans = prefix_sum[0];

    # Perform prefix sum and update
    # the ans to maximum
    for i in range(1, MAX):
        prefix_sum[i] += prefix_sum[i - 1];
        ans = max(ans, prefix_sum[i]);

    return ans;


# Driver code
if __name__ == "__main__":
    lectures = [[0, 5],
                [1, 2],
                [1, 10]];

    n = len(lectures);

    print(minHalls(lectures, n))
