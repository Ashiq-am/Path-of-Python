import numpy as np

# Importing csv module
import csv


with open("sample_data.csv", 'r') as x:
	sample_data = list(csv.reader(x, delimiter=","))

sample_data = np.array(sample_data)
display(sample_data)
