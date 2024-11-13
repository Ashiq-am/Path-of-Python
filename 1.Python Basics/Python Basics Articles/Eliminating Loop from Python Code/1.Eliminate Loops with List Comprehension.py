# Without list comprehension
square1 = []
for i in range(8):
	square1.append(i**2)

# With list comprehension
square2 = [i**2 for i in range(8)]

print("Using Loop: ", square1)
print("Using List Comprehension: ", square2)
