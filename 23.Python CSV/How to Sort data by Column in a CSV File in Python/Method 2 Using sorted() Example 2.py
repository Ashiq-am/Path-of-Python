# import modules
import csv ,operator

# load csv file
from tensorboard.notebook import display

data = csv.reader(open('sample.csv'),delimiter=',')

# sort data on the basis of age
data = sorted(data, key=operator.itemgetter(2), reverse=True)

# displaying sorted data
print('After sorting:')
display(data)
