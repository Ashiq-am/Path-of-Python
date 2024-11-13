file = 'input.txt'

# open the file in read mode
with open(file, 'r') as file:
    # read lines from the file
    lines = file.readlines()

# initialize an empty dictionary
res = {}

# iterate through each line and split key-value pairs
for line in lines:
    key, value = line.strip().split(':')
    res[key.strip()] = value.strip()

# print the dictionary
print("Dictionary Created:")
print(res)
