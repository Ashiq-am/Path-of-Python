# Importing library
import csv

# data to be written row-wise in csv fil
data = [['Geeks for Geeks', '2008', 'Sandeep Jain'],
		['HackerRank', '2009', 'Vivek Ravisankar']]

# opening the csv file in 'a+' mode
file = open('g4g.csv', 'a+', newline ='')

# writing the data into the file
with file:
	write = csv.writer(file)
	write.writerows(data)
