import yaml


def append_to_yaml(file_path, data_to_append):
	with open(file_path, 'a+') as file:
		file.seek(0)
		existing_data = yaml.load(file, Loader=yaml.FullLoader) or []
		existing_data.append(data_to_append)
		file.seek(0)
		yaml.dump(existing_data, file, default_flow_style=False)


file_path = 'data.yaml'
data_to_append = {'key': 'value'}
append_to_yaml(file_path, data_to_append)
