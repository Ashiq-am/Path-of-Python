# Python program to demonstrate
# command line arguments


import argparse

msg = "Adding description"

# Initialize parser
parser = argparse.ArgumentParser(description = msg)
parser.parse_args()
