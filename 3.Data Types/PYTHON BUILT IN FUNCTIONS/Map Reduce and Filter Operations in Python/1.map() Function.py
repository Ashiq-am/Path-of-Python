# Function to return double of n
def double(n):
    return n * 2

# Using map to double all numbers
numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))
