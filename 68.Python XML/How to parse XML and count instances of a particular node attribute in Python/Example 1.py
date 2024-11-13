# Importing our module
import xml.etree.ElementTree as ET


# Finding the Node Attribure with name tag
# neighbor and name value as "Germany"
Name_attribute = "France"

# Parsing our xml file
tree = ET.parse('country_data.xml')
root = tree.getroot()

# Counting the instance of Node attribute with findall
NO_node = 0
for instance in root.findall('country/neighbor'):
	# Checking for the particular Node Attribute
	if instance.get('name') == Name_attribute:
		NO_node+=1

# Printing Number of nodes
print ("total instance of given node attribute is : ", NO_node)
