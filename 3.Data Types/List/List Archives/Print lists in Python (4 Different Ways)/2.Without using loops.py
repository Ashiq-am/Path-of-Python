# Python program to print list
# without using loop

a = [1, 2, 3, 4, 5]

# printing the list using * operator separated
# by space
print(*a)

# printing the list using * and sep operator
print("printing lists separated by commas")

print(*a, sep = ", ")

# print in new line
print("printing lists in new line")

print(*a, sep = "\n")
