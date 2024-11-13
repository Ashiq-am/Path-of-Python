# Defining custom names for lists
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


# Dictonary to be converted
obj = {'mylist': [u'foo', u'bar', u'baz'],
	'mydict': {
				'foo': u'bar',
				'baz': 1},
	'ok': True}

# custom function for defining
# item names
my_item_func = lambda x: 'list_item'
xml = dicttoxml(obj, item_func = my_item_func)

# Pretty formating XML
xml_format = parseString(xml).toprettyxml()

print(xml_format)

