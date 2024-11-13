# i,j - loop variable

# loop-1
print("Using the loop variable inside :")

# used loop variable
for i in range(0, 5):

	x = (i+1)*2
	print(x, end=" ")

# loop-2
print("\nUsing the loop variable only for iteration :")

# unsused loop variable
for j in range(0, 5):

	print('*', end=" ")
