# Python program for demonstrating how
# to add the created network in an xml file

# Importing library
from pybrain.tools.customxml import NetworkWriter

# Creating myNetwork.xml file and
# saving the myNetwork into it
NetworkWriter.writeToFile(myNetwork,
						'myNetwork.xml')
