#import package
from collections import OrderedDict

# define OrderedDict
od1 = OrderedDict([('1', 'one'), ('2', 'two')])
print(type(od1))
print(od1)

# define nested OrderedDict
od2 = OrderedDict([('1', 'one'),
				('2', OrderedDict([('-2',
									'-ive'),
									('+2',
									'+ive')]))])
print(type(od2))
print(od2)
