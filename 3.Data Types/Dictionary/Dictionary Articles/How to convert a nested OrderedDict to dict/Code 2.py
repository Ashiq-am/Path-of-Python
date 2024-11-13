# import package
from collections import OrderedDict

# define OrderedDict
od1 = OrderedDict([('1', 'one'), ('2', 'two')])

# convert to dict
od1 = dict(od1)

# display dictionary
print(type(od1))
print(od1)
