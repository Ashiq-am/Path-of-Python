a = [1, 'geeks', 3, 'for', 5]

# Accessing elements from index 1 to 3 (excluding 4)
a1 = a[1:4]  # ['geeks', 3, 'for']

# Accessing elements from start to index 3 (excluding 4)
a2 = a[:4]  # [1, 'geeks', 3, 'for']

# Accessing elements from index 2 to the end
a3 = a[2:]  # [3, 'for', 5]

# Accessing every second element
a4 = a[::2]  # [1, 3, 5]

print(a1, a2, a3, a4)