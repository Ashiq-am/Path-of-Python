import json
from collections import OrderedDict


#create Ordered Dictionary using keyword
# 'object_pairs_hook=OrderDict'
data = json.loads('{"GeeksforGeeks":1, "Gulshan": 2, "nightfury_1": 3, "Geek": 4}',
				object_pairs_hook=OrderedDict)
print("Ordered Dictionary: ", data)
