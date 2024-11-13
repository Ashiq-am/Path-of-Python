import json

import var as var

with open("Sample.json", "w") as p:
	json.dumps(var, p)




'''Here, the dumps() takes two arguments first, the data object to be serialized and second the 
object to which it will be written(Byte format)'''
