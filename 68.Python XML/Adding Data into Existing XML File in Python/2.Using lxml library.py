from lxml import etree

# Load the existing XML file
tree = etree.parse("sample.xml")
root = tree.getroot()

# Append new data
new_item = etree.SubElement(root, "item")
new_item.attrib["id"] = "3"
new_item.text = "Item 3"

# Save the changes back to the file
tree.write("sample.xml", pretty_print=True)
