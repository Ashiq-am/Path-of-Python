import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7])

# Find all even numbers using filter
li = list(filter(lambda x: x % 2 == 0, arr))

print(li)