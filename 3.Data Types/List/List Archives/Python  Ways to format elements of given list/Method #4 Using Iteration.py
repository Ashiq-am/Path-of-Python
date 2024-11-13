# Python code to truncate float
# values to 2 decimal digits.

# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

# Output list initialization
Output = []

# Iterating
for elem in Input:
	Output.append("%.2f" % elem)

# Printing output
print(Output)
