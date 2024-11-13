class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def fractional_knapsack_dynamic(items, capacity):
    n = len(items)

    # Initialize dp array to store maximum value achieved for each capacity
    dp = [0] * (capacity + 1)

    # Iterate from 1 to capacity
    for i in range(1, capacity + 1):
        max_value = 0
        # Iterate through each item
        for j in range(n):
            if items[j].weight <= i:
                # Update max_value with the maximum value achieved for the current capacity
                max_value = max(max_value, dp[i - items[j].weight] + items[j].value)
        # Update dp array with the maximum value achieved for current capacity
        dp[i] = max_value

        # Return maximum profit achieved using dynamic programming
    return dp[capacity]


# Example usage
items = [
    Item(10, 60),
    Item(20, 100),
    Item(30, 120)
]
capacity = 50
print("Maximum Value Obtained Using Dynamic Approach is", fractional_knapsack_dynamic(items, capacity))
