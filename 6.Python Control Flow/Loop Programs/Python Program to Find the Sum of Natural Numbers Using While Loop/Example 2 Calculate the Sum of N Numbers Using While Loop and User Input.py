# Takes the input of N given by the user
N = int(input("Enter the value of N: "))

# Initialize the variables 'count' and 'total'
count = N
total = 0

while count:
	total += count
	count -= 1

# Prints the sum of N natural numbers.
print("The sum of the first", N, "natural numbers is:", total)
