# Python Program to
# show range() basics

# printing a number
for i in range(10):
	print(i, end =" ")
print()

# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
	print(l[i], end =" ")
print()

# performing sum of natural
# number
sum = 0
for i in range(1, 11):
	sum = sum + i
print("Sum of first 10 natural number :", sum)
