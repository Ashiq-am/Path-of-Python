# Python code to split list containing single integer

# List initialization
input = [987]

# Converting to int
input = int(input[0])

# Output list initialization
output = []

while input>0:
	rem = input % 10
	input = int(input / 10)
	output.append(rem)

# Printing output
print(output)
