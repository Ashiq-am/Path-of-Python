# Converting Python Dictionary to XML
# with a root elemtnt
from dict2xml import dict2xml


data = {'a': 2,
		'b': {
			'c': 'as',
			'f': True},
		'd': 7,
		}

xml = dict2xml(data, wrap ='root', indent =" ")
print(xml)
