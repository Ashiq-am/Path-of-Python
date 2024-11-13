# To encode and decode operations
import json
var ={'age':31,'height':6}
x = json.dumps(var)
y = json.loads(var)
print(x)
print(y)

# when performing from a file in disk
with open("any_file.json", "r") as readit:
	x = json.load(readit)
print(x)

