# import modules
import csv ,operator

# load csv file
data = csv.reader(open('sample.csv'),delimiter=',')

# sort data on the basis of age
data = sorted(data, key=operator.itemgetter(2))

# displaying sorted data
print('After sorting:')
display(data)
