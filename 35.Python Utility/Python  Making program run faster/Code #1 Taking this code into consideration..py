''''''

'''
# abc.py
import sys
import csv

with open(sys.argv[1]) as f:
    for row in csv.reader(f):
# Some kind of processing

'''
