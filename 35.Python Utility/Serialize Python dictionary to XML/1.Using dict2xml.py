# Converting Python Dictionary to XML
from dict2xml import dict2xml


data = {'a': 2,
		'b': {
			'c': 'as',
			'f': True},
		'd': 7,
		}

xml = dict2xml(data)
print(xml)
