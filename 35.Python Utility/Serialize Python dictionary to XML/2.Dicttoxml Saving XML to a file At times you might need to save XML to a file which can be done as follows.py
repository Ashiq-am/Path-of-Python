# Converting Python Dictionary to
# XML and saving to a file
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


# Variable name of Dictionary is data
xml = dicttoxml(data)

# Obtain decode string by decode()
# function
xml_decode = xml.decode()

xmlfile = open("dict.xml", "w")
xmlfile.write(xml_decode)
xmlfile.close()
