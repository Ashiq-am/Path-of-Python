import matplotlib.pyplot as plt
import csv

X = []
Y = []

with open('GFG.txt', 'r') as datafile:
	ploting = csv.reader(datafile, delimiter=',')
