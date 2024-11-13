# importing the module.
import xml.etree.ElementTree as ET
XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
<COUNTRIES>
	<country name ="INDIA">
		<neighbor name ="Dubai" direction ="W"/>
	</country>
	<country name ="Singapore">
		<neighbor name ="Malaysia" direction ="N"/>
	</country>
</COUNTRIES>
'''
# parsing directly.
tree = ET.parse('xmldocument.xml')
root = tree.getroot()
# parsing using the string.
stringroot = ET.fromstring(XMLexample_stored_in_a_string)
# printing the root.
print(root)
print(stringroot)
