# Python program to print first 10
# prime numbers

# A function name prime is defined
# using def
def prime(n):
	x = 1
	count = 0
	while count < n:
		for d in range(2, x, 1):
			if x % d == 0:
				x += 1
		else:
			print(x)
			x += 1
			count += 1

# Driver Code
n = 10

# print statement
print("First 10 prime numbers are: ")
prime(n)
