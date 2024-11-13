# import package
from collections import OrderedDict
import json

# define OrderedDict
od1 = OrderedDict([('1','one'),
				('2','two')])

# check type i.e; OrderedDict
print(type(od1))

# convert to json
od1 = json.dumps(od1)

# check type i.e; str
print(type(od1))

# view value
print(od1)
