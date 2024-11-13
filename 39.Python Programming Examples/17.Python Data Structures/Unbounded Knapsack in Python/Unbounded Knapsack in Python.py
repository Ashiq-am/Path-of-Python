def unbounded_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(capacity + 1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])

    return dp[capacity]


# Example usage
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8
max_value = unbounded_knapsack(weights, values, capacity)
print(f"The maximum value obtainable is: {max_value}")
