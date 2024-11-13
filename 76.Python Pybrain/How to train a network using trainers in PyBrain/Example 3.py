# Python program to demonstrate how to train
# a network

# Importing libraries and packages
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# Establishing a network having two inputs,
# four hidden, and one output channels
network = buildNetwork(2, 4, 1, bias=True, hiddenclass=TanhLayer)

# Creating a dataset that match with the
# network input and output sizes
nand_gate = SupervisedDataSet(2, 1)

# Creating a dataset for testing
nand_train = SupervisedDataSet(2, 1)

# Fit input and target values to dataset
# Parameters for nand_train truth table
nand_gate.addSample((0, 0), (1,))
nand_gate.addSample((0, 1), (1,))
nand_gate.addSample((1, 0), (1,))
nand_gate.addSample((1, 1), (0,))

# Fit input and target values to dataset
# Parameters for nand_train truth table
nand_train.addSample((0, 0), (1,))
nand_train.addSample((0, 1), (1,))
nand_train.addSample((1, 1), (1,))
nand_train.addSample((1, 1), (0,))

# Training the network with dataset nand_gate
trainer = BackpropTrainer(network, nand_gate)

# Iterate 10 times to train the network
for epoch in range(100):
	trainer.train()
	trainer.testOnData(dataset=nand_train, verbose=True)
