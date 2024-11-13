def infinite_geometric_sum(a1, r):
    if abs(r) >= 1:
        return float('inf')  # or raise an exception
    return a1 / (1 - r)

# Example usage
a1 = 2
r = 0.5
infinite_sum = infinite_geometric_sum(a1, r)
print("Sum of Infinite Geometric Series:", infinite_sum)
