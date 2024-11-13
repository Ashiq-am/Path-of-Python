# importing the module
import argparse

# creating an ArgumentParsert object
parser = argparse.ArgumentParser()

# fetching the arguments
parser.add_argument('number',
					help = "Enter number to triple it.")
args = parser.parse_args()

# performing some operation
print(args.number * 2)
