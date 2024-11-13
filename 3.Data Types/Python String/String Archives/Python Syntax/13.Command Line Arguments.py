# import sys module
import sys

if len(sys.argv) < 2:
	print("Please provide numbers as arguments to sum.")
	sys.exit(1)

try:
	# Convert arguments to integers and sum them
	total = sum(map(float, sys.argv[1:]))
	print(f"Sum: {total}")
except ValueError:
	print("All arguments must be valid numbers.")
