# Using a for loop to create a list of squares
squares = []
for n in range(50000):
	squares.append(n ** 2)
print(squares)

# Using a generator expression
# Reduced to 10 for brevity
squares_gen = (n ** 2 for n in range(50000))
for square in squares_gen:
	print(square, end=' ')
