# Python code to sort list of percentage

# List initialization
Input =['2.5 %', '6.4 %', '91.6 %', '11.5 %']

# Temporary list initialization
temp = []

# removing % sign
for key in Input:
	temp.append((key[:-1]))

# sorting list of float
temp = sorted(temp, key = float)

# Output list initialization
output = []

# Adding percentage sign
for key in temp:
	output.append(key + '%')

# printing output
print(output)
