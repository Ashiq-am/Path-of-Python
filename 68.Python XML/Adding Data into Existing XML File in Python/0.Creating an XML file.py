import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("data")

# Create a child element with attributes
item = ET.SubElement(root, "item")
item.attrib["id"] = "1"
item.text = "Item 1"

# Create another child element
item = ET.SubElement(root, "item")
item.attrib["id"] = "2"
item.text = "Item 2"

# Create the tree and write it to a file
tree = ET.ElementTree(root)
tree.write("sample.xml")
