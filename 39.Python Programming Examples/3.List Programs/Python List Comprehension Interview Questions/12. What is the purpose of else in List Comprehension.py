# List comprehension that checks if each number in the range is positive.

a = [x if x > 0 else 0 for x in range(-3, 3)]
print(a)