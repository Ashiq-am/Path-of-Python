# import the python pandas library
import pandas as pd

# use pandas read_csv() function to read the dataset.
data = pd.read_csv("AirPassengers.csv", header=0, index_col=0)

# extracting only the air passengers count from
# the dataset using values function
values = data.values

# getting the count to split the dataset into 3
parts = int(len(values)/3)

# splitting the data into three parts
part_1, part_2, part_3 = values[0:parts], values[parts:(
	parts*2)], values[(parts*2):(parts*3)]

# calculating the mean of the seperated three
# parts of data induvidually.
mean_1, mean_2, mean_3 = part_1.mean(), part_2.mean(), part_3.mean()

# calculating the variance of the seperated
# three parts of data induvidually.
var_1, var_2, var_3 = part_1.var(), part_2.var(), part_3.var()

# printing the mean of three groups
print('mean1=%f, mean2=%f, mean2=%f' % (mean_1, mean_2, mean_3))

# printing the variance of three groups
print('variance1=%f, variance2=%f, variance2=%f' % (var_1, var_2, var_3))
