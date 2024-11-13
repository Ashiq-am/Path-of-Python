# import package
from collections import OrderedDict
import json

# define nested OrderedDict
od2 = OrderedDict([('1', 'one'),
				('2', OrderedDict([('-2',
									'-ive'),
									('+2',
									'+ive')]))])
# convert to dict
od2 = json.loads(json.dumps(od2))

# display deictionary
print(type(od2))
print(od2)
