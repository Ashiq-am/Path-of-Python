# Python program to demonstrate
# command line arguments


import argparse


# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show Output")

# Read arguments from command line
args = parser.parse_args()

if args.Output:
	print("Diplaying Output as: % s" % args.Output)
