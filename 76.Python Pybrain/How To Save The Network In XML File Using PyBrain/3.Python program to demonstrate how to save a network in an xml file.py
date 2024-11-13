# Python program to demonstrate
# how to save a network in an xml file

# gfg.py
# Import libraries

from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.customxml import NetworkWriter

# Creating a network
# This network has two inputs,
# four hidden and one output neuron
myNetwork = buildNetwork(2, 4, 1)

# Creating myNetwork.xml file and
# saving the myNetwork into it
NetworkWriter.writeToFile(myNetwork, 'myNetwork.xml')
