# Python program to demonstrate how to
# optimize a network using Optimization
# algorithms in PyBrain

# Importing library
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization.populationbased.ga import GA

# Creating OR dataset
orDataset = ClassificationDataSet(2)

# Inserting sample to orDataset
orDataset.addSample([0., 0.], [0.])
orDataset.addSample([0., 1.], [1.])
orDataset.addSample([1., 0.], [1.])
orDataset.addSample([1., 1.], [1.])

# Set the target field
orDataset.setField('class', [[0.], [1.], [1.], [1.]])


# Building a network
# The network consists of two input layers,
# four hidden layers and one output layer
myNetwork = buildNetwork(2, 4, 1)

# GA optimization algorithm
gaOptimization = GA(orDataset.evaluateModuleMSE,
					myNetwork, minimize=True)

# 100 iterations for learning
for i in range(100):
	myNetwork = gaOptimization.learn(0)[0]

# By passing input optimize the network
print(myNetwork.activate([0, 0]))
print(myNetwork.activate([1, 0]))
print(myNetwork.activate([0, 1]))
print(myNetwork.activate([1, 1]))
