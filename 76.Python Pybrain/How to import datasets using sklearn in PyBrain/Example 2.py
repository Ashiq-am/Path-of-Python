# Importing libraries
from sklearn import datasets
from pybrain.datasets import ClassificationDataSet

# Loading iris
loaded_digits = datasets.load_iris()

# Setting data fields
x_data, y_data = loaded_digits.data, loaded_digits.target

# Creating a ClassificationDataset
dataset = ClassificationDataSet(4, 1, nb_classes=2)

# Iterating over the length of x_data
for i in range(len(x_data)):
	dataset.addSample(x_data[i], y_data[i])

# Print the dataset
print(dataset)
