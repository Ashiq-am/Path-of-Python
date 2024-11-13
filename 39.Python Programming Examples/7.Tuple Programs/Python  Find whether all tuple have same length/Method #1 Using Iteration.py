# Python code to find whether all
# tuple have equal length

# Input List initialization
Input = [(11, 22, 33), (44, 55, 66)]

# printing
print("Initial list of tuple", Input)

# K Intilization
k = 3
flag = 1

# Iteration
for tuple in Input:
	if len(tuple) != k:
		flag = 0
		break

# Checking whether all tuple
# have length equal to 'K' in list of tuple
if flag:
	print("All tuples have same length")
else:
	print("Tuples does not have same length")
