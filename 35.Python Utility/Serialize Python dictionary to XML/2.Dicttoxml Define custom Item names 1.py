# Using parent name in dictionary
# as tag name in xml

from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# Dictionary to be converted
data = {
	'month':['Jan', 'Feb',
			'Mar', 'Apr',
			'May', 'Jun',
			'Jul', 'Aug',
			'Sep', 'Oct',
			'Nov', 'Dec']
	}

# Here x is the parent, you can chose
# to do some prcessing or use a part
# of the parent name for tag name
my_item_func = lambda x: x+'s'
xml = dicttoxml(data, item_func = my_item_func)

print(parseString(xml).toprettyxml())
