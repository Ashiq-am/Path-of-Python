# Initial list
a = [10, 20, 30, 40, 50]

# Index of the element to remove
idx = 2

# Removing element using list comprehension
a = [item for i, item in enumerate(a) if i != idx]

print(a)