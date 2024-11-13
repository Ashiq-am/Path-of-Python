import yaml

file = 'input.txt'

# open the file in read mode
with open(file, 'r') as file:
	# load data from yaml
	res = yaml.safe_load(file)

# print the dictionary
print("Dictionary Created")
print(res)
