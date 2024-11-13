# import required modules
import json
from collections import OrderedDict

# assign json file
jsonFile = '{"Geeks":1, "for": 2, "geeks":3}'
print(jsonFile)

# convert to Ordereddict
data = json.loads(jsonFile,object_pairs_hook=OrderedDict)
print(data)
