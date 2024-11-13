# Python program to demonstrate how to create a network
# Import libraries

from pybrain.tools.shortcuts import buildNetwork

# Creating a network
# This network has two inputs, four hidden
# and one output neuron
myNetwork = buildNetwork(2, 4, 1)

print(myNetwork)
