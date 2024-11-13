# Python program to create a classification dataset

# importing library
from pybrain.datasets.classification import ClassificationDataSet

# Creating OR dataset
orDataset = ClassificationDataSet(2)

# Inserting sample to orDataset
orDataset.addSample([0., 0.], [0.])
orDataset.addSample([0., 1.], [1.])
orDataset.addSample([1., 0.], [1.])
orDataset.addSample([1., 1.], [1.])

# Set the target field
orDataset.setField('class', [[0.],[1.],[1.],[1.]])
