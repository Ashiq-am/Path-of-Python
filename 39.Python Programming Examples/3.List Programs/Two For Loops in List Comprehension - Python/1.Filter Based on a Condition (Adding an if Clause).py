x = [1, 2, 3]
y = [3, 4, 5]

# Using two for loops and an if condition to filter
ans = [(a, b) for a in x for b in y if a + b > 4]

print(ans)