# Other Method of Encoding
import json

json.JSONEncoder().encode({"foo": ["bar"]})
'{"foo": ["bar"]}'

# Using iterencode(object) to encode a given object.
for i in json.JSONEncoder().iterencode(bigobject):
	mysocket.write(i)
