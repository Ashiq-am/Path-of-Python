import sys

# Save the original stdout
original_stdout = sys.stdout

# Redirect stdout to a file
with open('output.txt', 'w') as f:
	sys.stdout = f
	for i in range(10):
		print("printing line ", i)
