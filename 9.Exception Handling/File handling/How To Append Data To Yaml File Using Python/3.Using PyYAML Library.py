import yaml

def append_to_yaml(file_path, data_to_append):
	with open(file_path, 'a') as file:
		yaml.dump(data_to_append, file)

file_path = 'data.yaml'
data_to_append = {'key': 'value'}
append_to_yaml(file_path, data_to_append)
