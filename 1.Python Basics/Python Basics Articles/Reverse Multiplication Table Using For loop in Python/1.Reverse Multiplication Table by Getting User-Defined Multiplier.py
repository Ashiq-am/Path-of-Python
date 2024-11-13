print("Enter the number of multiplication table to print:")

# Getting the number of multiplication table from user
tableNumber = int(input())

print("Printing Multiplication Table of", tableNumber, "in Reverse Order")

# Using For loop to print Multiplication table from number 10 to 1 of user input number
for num in range(10, 0, -1):
	print(num, "*", tableNumber, " =", (num * tableNumber))
