import json

with open('exam.json','r') as json_File :
	sample_load_file=json.load(json_File)
print(sample_load_file)
