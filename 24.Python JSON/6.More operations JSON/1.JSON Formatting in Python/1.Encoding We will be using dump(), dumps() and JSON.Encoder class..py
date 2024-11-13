#Code will run in Python 3

from io import StringIO
import json

fileObj = StringIO()
json.dump(["Hello", "Geeks"], fileObj)
print("Using json.dump(): "+str(fileObj.getvalue()))

class TypeEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, type):
			return str(obj)

print("Using json.dumps(): "+str(json.dumps(type(str), cls=TypeEncoder)))
print("Using json.JSONEncoder().encode"+
	str(TypeEncoder().encode(type(list))))
print("Using json.JSONEncoder().iterencode"+
	str(list(TypeEncoder().iterencode(type(dict)))))
