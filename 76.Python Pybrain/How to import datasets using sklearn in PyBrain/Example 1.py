# Importing libraries
from sklearn import datasets
from pybrain.datasets import ClassificationDataSet

# Loading digits
loaded_digits = datasets.load_digits()

# Set data items
x_data, y_data = loaded_digits.data, loaded_digits.target

# Classification dataset
dataset = ClassificationDataSet(64, 1, nb_classes=15)

# Iterate over the length of X
for i in range(len(x_data)):
	dataset.addSample(x_data[i], y_data[i])

# Print the dataset
print(dataset)
