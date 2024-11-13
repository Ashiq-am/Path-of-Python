# Importing our module
from xml.dom import minidom

# Finding the node instance with name "Germany"
Name_attribute = "Germany"

# Parsing our xml file
doc = minidom.parse('country_data.xml')
root = doc.getElementsByTagName('neighbor')

Number_attributes = 0
for i in root:
    # print ctypes.cast(i, ctypes.py_object).value
    if i.attributes['name'].value == Name_attribute:
        Number_attributes += 1

# Printing Number of nodes
print("Total instance of Particular node attribute is : ", Number_attributes)
