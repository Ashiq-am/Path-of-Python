a = []
b = []

# initialize the spaces with 0’s with
# the help of list comprehensions
a = [0 for x in range(10)]
print(a)

# initialize multi-array
b = [[None for y in range(2)]
     for x in range(2)]

print(b)
