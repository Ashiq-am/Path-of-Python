# Python program to approximate
# the cube root of 27
guess = 0.0
cube = 27
increment = 0.0001
epsilon = 0.1

# Finding the approximate value
while abs(guess**3 - cube) >= epsilon:
	guess+=increment

# Checking the approximate value
if abs(guess**3 - cube) >= epsilon:
	print("Failed on the cube root of",cube)
else:
	print(guess,"is close to the cube root of",cube)
