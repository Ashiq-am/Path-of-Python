x1 = [10, 20, 30]

# Here a new list x2 is created using x1
x2 = list(x1)

# The "==" operator would produce "Yes"
if x1 == x2:
	print("Yes")
else:
	print("No")

# But "is" operator would produce "No"
if x1 is x2:
	print("Yes")
else:
	print("No")
