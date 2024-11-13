import sys

# Exit the program with an error message
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
print("Processing file:", input_file)