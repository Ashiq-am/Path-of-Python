# Python code to demonstrate naive method
# using loop

# function returning binary string
def Binary(n):
	binary = ""
	i = 0
	while n > 0 and i<=8:
		s1 = str(int(n%2))
		binary = binary + s1
		n /= 2
		i = i+1
		d = binary[::-1]
	return d

print("The binary representation of 100 (using loops) is : ",end="")
print(Binary(100))
