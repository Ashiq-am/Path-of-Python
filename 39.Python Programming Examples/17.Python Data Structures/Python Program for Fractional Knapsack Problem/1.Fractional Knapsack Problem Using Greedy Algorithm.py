class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        # Calculate the value-to-weight ratio for each item
        self.ratio = value / weight


def fractional_knapsack(items, capacity):
    # Sort items by their value-to-weight ratio in non-increasing order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0

    # Initialize remaining capacity of the knapsack
    remaining_capacity = capacity

    # Iterate through the sorted items list
    for item in items:
        if remaining_capacity <= 0:
            break

        # Calculate fraction of the item that fits into the knapsack
        fraction = min(1, remaining_capacity / item.weight)

        # Update total value and remaining capacity
        total_value += fraction * item.value
        remaining_capacity -= fraction * item.weight

    # Return total maximum value obtained
    return round(total_value, 2)


# Example usage
items = [
    Item(10, 60),
    Item(20, 100),
    Item(30, 120)
]
capacity = 50
print("Maximum Value that can be Obtained is", fractional_knapsack(items, capacity))
