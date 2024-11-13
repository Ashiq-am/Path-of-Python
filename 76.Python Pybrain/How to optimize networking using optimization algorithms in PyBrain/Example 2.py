# Python program to create a network

from pybrain.tools.shortcuts import buildNetwork

# Building a network
# The network consists of two input layers,
# four hidden layers and one output layer
myNetwork = buildNetwork(2, 4, 1)
