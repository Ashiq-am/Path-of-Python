import xml.etree.ElementTree as ET

# Load the existing XML file
tree = ET.parse("sample.xml")
root = tree.getroot()

# Append new data
new_item = ET.SubElement(root, "item")
new_item.attrib["id"] = "3"
new_item.text = "Item 3"

# Save the changes back to the file
tree.write("sample.xml")
