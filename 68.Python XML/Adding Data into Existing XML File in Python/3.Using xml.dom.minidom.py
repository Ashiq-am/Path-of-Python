import xml.dom.minidom

# Load the existing XML file
doc = xml.dom.minidom.parse("sample.xml")
root = doc.documentElement

# Append new data
new_item = doc.createElement("item")
new_item.setAttribute("id", "3")
text_node = doc.createTextNode("Item 3")
new_item.appendChild(text_node)
root.appendChild(new_item)

# Save the changes back to the file
with open("sample.xml", "w") as file:
    doc.writexml(file)
