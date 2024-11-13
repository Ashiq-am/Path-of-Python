# Removing Type Attribute from parsed XML
from xml.dom.minidom import parseString

# attr_type = False is used
# to remove type attributes
xml = dicttoxml(data, attr_type = False)

print(parseString(xml).toprettyxml())
