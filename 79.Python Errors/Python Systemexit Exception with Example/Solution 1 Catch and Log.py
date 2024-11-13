import sys

try:
	# Code that may raise SystemExit
	sys.exit("Exiting the program")
except SystemExit as e:
	print(f"Caught SystemExit: {e}")

# Continue with the program execution if needed
print("Program continues after handling SystemExit")
