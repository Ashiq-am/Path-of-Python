# Pretty printing XML after parsing
# it from dictionary
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


# Data to be parsed
data = {'a': 2,
		'b': {
			'c': 'as',
			'f': True},
		'd': 7,
		}

xml = dicttoxml(data)
dom = parseString(xml)

print(dom.toprettyxml())
