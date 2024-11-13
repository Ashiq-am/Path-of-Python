''''''



'''
# abc.py
import sys
import csv

def main(filename):
	with open(filename) as f:
		for row in csv.reader(f):
		# Some kind of processing

main(sys.argv[1])



'''