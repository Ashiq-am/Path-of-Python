# Get number of elements to input
n = int(input("Number of elements: "))

# Initialize an empty list
a = []

# Use a for loop to take input from user
for i in range(n):
    # Collect input for each element
    val = input()
    a.append(val)

print(a)