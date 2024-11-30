a = "123"

length = 6
# Calculate how many zeros to add
zeros_needed = length - len(a)
# Add zeros to the left
result = "0" * zeros_needed + a
print(result)