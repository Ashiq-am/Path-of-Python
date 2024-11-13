# Python 3 code to demonstrate
# property of iter()

# initializing list
lis1 = [1, 2, 3, 4, 5]

# converting list using iter()
lis1 = iter(lis1)

# prints this
print("Values at 1st iteration : ")
for i in range(0, 5):
	print(next(lis1))

# doesn't print this
print("Values at 2nd iteration : ")
for i in range(0, 5):
	print(next(lis1))
