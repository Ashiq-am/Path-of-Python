# Python code to find whether all tuple
# have equal length

# Input list initilization
Input = [(11, 22, 33), (44, 55, 66), (11, 23)]
k = 2

# Printing
print("Initial list of tuple", Input)

# Using all()
Output =(all(len(elem) == k for elem in Input))

# Checking whether all tuple
# have equal length
if Output:
	print("All tuples have same length")
else:
	print("Tuples does not have same length")
