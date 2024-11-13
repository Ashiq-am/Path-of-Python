# importing the module
import argparse

# creating an ArgumentParsert object
parser = argparse.ArgumentParser()

# fetching the arguments
parser.add_argument('number',
					help = "Enter number to double.",
					type = int)
args = parser.parse_args()
print(args.number * 2)
