# importing packages and modules
import pandas as pd
import scipy.stats as stats

# reading CSV file
dataset = pd.read_csv('iris.csv')

# data which contains sepal width of the three species
data = [dataset[dataset['species'] == "setosa"]['sepal_length'],
		dataset[dataset['species'] == "versicolor"]['sepal_length'],
		dataset[dataset['species'] == "virginica"]['sepal_length']]

# performing Bartlett's test
test_statistic, p_value = stats.bartlett(data[0], data[1], data[2])

print(test_statistic, p_value)
