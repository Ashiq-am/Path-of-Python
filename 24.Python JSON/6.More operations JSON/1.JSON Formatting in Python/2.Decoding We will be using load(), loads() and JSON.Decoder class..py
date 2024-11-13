#Code will run in Python 3

from io import StringIO
import json

fileObj = StringIO('["Geeks for Geeks"]')
print("Using json.load(): "+str(json.load(fileObj)))
print("Using json.loads(): "+str(json.loads('{"Geeks": 1, "for": 2, "Geeks": 3}')))
print("Using json.JSONDecoder().decode(): " +
	str(json.JSONDecoder().decode('{"Geeks": 1, "for": 2, "Geeks": 3}')))
print("Using json.JSONDecoder().raw_decode(): " +
	str(json.JSONDecoder().raw_decode('{"Geeks": 1, "for": 2, "Geeks": 3}')))
