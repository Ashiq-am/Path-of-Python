nums = [1, 2, 3]
chars = ['a', 'b', 'c']
combined = [f"{num}{char}" for num in nums for char in chars]
print(combined)